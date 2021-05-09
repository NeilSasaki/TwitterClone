from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    # メールアドレスがユーザーを一意に識別することにする
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)

class RegistForm(forms.ModelForm):
    username = forms.CharField(label='Name')
    email = forms.EmailField(label='E-mail address')
    password = forms.CharField(label='Passoword', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username','email', 'password']

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
