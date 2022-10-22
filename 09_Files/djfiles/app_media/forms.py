from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_media.models import Profile, Entry

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    email = forms.EmailField(required=False, help_text='Почта')
    number = forms.IntegerField(required=False, help_text='Номер телефона', min_value=100000, max_value=99999999999)
    city = forms.CharField(max_length=30, required=False, help_text='Город')


class RegisterFormUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('number', 'city')


class EntryForm(forms.Form):
    name = forms.CharField(max_length=50, help_text='Название записи')
    description = forms.CharField(widget=forms.Textarea, max_length=1000, help_text='Описание')
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True})
                              , help_text='Файлы', required=False)


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()

