from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'avatar', 'first_name', 'last_name', 'user_info', 'phone_number', 'gender')
    search_fields = ('username', 'email', 'first_name')


admin.site.register(CustomUser, CustomUserAdmin)
