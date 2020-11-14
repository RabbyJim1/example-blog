from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        # model = get_user_model()
        fields = UserChangeForm.Meta.fields


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
