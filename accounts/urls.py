from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import UserDetailView, RegisterView, UserSearchView, UserUpdateView

app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<int:pk>/edit/', UserUpdateView.as_view(), name='edit_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_search/', UserSearchView.as_view(), name='user_search'),
]
