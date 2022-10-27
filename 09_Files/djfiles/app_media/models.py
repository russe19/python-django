from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, verbose_name=_('Phone number'))
    city = models.CharField(max_length=30, blank=True, verbose_name=_('City'))

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')

class Entry(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), default=None, null=True, on_delete=models.CASCADE,
                             related_name='user')
    name = models.CharField(max_length=50, verbose_name=_('Entry name'), blank=True, null=True)
    description = models.TextField(max_length=1000, verbose_name=_('Description'))
    created_at = models.DateField(verbose_name=_('Date create'), default=datetime.date.today())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('entres')
        verbose_name = _('entry')

class EntryImage(models.Model):
    entry = models.ForeignKey(Entry, verbose_name=_('Entry'), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = _('entryimages')
        verbose_name = _('entryimage')


