from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')

class Entry(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', default=None, null=True, on_delete=models.CASCADE,
                             related_name='user')
    name = models.CharField(max_length=50, verbose_name='Запись', blank=True, null=True)
    description = models.TextField(max_length=1000, verbose_name='Описание записи')
    created_at = models.DateField(verbose_name='Время создания', default=datetime.date.today())

    def __str__(self):
        return self.name

class EntryImage(models.Model):
    entry = models.ForeignKey(Entry, verbose_name='Запись', on_delete=models.CASCADE, related_name='entry')
    image = models.ImageField(upload_to='images/')


