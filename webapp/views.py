from django.shortcuts import render
from django.utils import timezone
from django.utils.timesince import timesince

from webapp.models import Post


def home(request):
    posts = Post.objects.all()

    for post in posts:
        post.time_since_post = timesince(post.pub_date, timezone.now())

    return render(request, 'home.html', {'posts': posts})
