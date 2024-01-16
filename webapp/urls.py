from django.urls import path
from webapp.views import home, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]