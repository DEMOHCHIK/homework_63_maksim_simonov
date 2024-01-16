from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'image', 'like_count', 'comment_count')
    search_fields = ('title', 'author__username')


admin.site.register(Post, PostAdmin)
