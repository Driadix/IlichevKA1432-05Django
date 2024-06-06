# main/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import Comment, News


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Ваш комментарий'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Подтвердите новый пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image']
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'image': 'Изображение',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }