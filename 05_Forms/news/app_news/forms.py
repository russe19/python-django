from django import forms
from app_news.models import News, Comment


class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = ['name', 'description', 'is_active']


class CommentForm(forms.Form):

    user_name = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)

