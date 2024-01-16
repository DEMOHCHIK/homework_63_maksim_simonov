from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.timesince import timesince
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from webapp.forms import PostForm
from webapp.models import Post


def home(request):
    posts = Post.objects.all()

    for post in posts:
        post.time_since_post = timesince(post.pub_date, timezone.now())

    return render(request, 'home.html', {'posts': posts})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('webapp:post_detail', pk=post.pk)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'

    def get_success_url(self):
        return reverse_lazy('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('webapp:home')

    def get_cancel_url(self):
        return reverse_lazy('webapp:post_detail', kwargs={'pk': self.object.pk})
