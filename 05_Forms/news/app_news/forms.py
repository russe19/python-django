from django import forms
from app_news.models import News, Comment


class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.Form):

    user_name = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)

    # class Meta:
    #     model = News
    #     fields = ['user_name', 'text']

