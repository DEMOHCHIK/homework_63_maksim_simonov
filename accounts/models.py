from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, verbose_name='Логин', unique=True)
    email = models.EmailField(unique=True, verbose_name='Адрес электронной почты')
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватар')
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True, null=True)
    user_info = models.TextField(blank=True, null=True, verbose_name='Информация о пользователе')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=20, choices=[('man', 'Муж'), ('woman', 'Жен'), ('other', 'Другой')],
                              blank=True, null=True, verbose_name='Пол')

    def __str__(self):
        return self.username
