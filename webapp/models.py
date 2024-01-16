from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True,)
    description = models.TextField(blank=True, null=True,)
    image = models.ImageField(upload_to='images')
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
