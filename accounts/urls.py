from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import UserProfileDetailView, RegisterView, UserSearchView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_search/', UserSearchView.as_view(), name='user_search'),
]
