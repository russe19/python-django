from django import forms
from app_news.models import News, Comment


class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.Form):
    # def __init__(self, news_id, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)

    user_name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

