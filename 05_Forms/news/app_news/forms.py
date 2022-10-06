from django import forms
from app_news.models import News, Comment


class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = ['name', 'description', 'is_active']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_name', 'text']


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


