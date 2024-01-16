from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            'email', 'password', 'avatar', 'first_name', 'last_name', 'user_info', 'phone_number', 'gender')


class UserSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Поиск',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'value': ''})
    )