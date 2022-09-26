from django import forms
from app_news.models import News, Comment


class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = '__all__'