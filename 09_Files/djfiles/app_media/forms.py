from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_media.models import Profile, Entry
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=_('First name'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('Last name'))
    email = forms.EmailField(required=False, help_text=_('Email'))
    number = forms.IntegerField(required=False, help_text=_('Number phone'), min_value=100000, max_value=99999999999)
    city = forms.CharField(max_length=30, required=False, help_text=_('City'))


class RegisterFormUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('number', 'city')


class EntryForm(forms.Form):
    name = forms.CharField(max_length=50, help_text=_('Entry name'))
    description = forms.CharField(widget=forms.Textarea, max_length=1000, help_text=_('Description'))
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True})
                              , help_text=_('Files'), required=False)


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50, help_text=_('file name'))
    file = forms.FileField(help_text=_('file'))

