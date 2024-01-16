from django.urls import path
from webapp.views import home

app_name = 'webapp'

urlpatterns = [
    path('', home),
    path('home/', home, name='home')
]