from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import News, Comment

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    email = forms.EmailField(required=False, help_text='Почта')
    number = forms.IntegerField(help_text='Номер телефона', min_value=100000, max_value=99999999999)
    city = forms.CharField(max_length=30, help_text='Город')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = ['name', 'description', 'tag']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_name', 'text']