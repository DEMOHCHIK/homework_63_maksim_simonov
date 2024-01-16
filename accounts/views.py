from django.contrib.auth import get_user_model, login
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, FormView, UpdateView

from accounts.forms import MyUserCreationForm, UserSearchForm, UserProfileForm
from webapp.models import Post


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(author=user)
        return context


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'user_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:home')
        return next_page


class UserUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'user_edit.html'

    def get_success_url(self):
        return reverse_lazy('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserSearchView(ListView, FormView):
    model = get_user_model()
    template_name = 'user_search.html'
    context_object_name = 'users'
    form_class = UserSearchForm

    def get_queryset(self):
        search_query = self.request.GET.get('search_query', '')
        if search_query:
            return get_user_model().objects.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(first_name__icontains=search_query)
            )
        return get_user_model().objects.none()

