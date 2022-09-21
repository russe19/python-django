from django.db import models
from django.utils import timezone
from datetime import timedelta

class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=1500, db_index=True)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(verbose_name='Время создания', auto_now_add=True)
    upadeted_at = models.DateField(verbose_name='Время снятия', default=timezone.now() + timedelta(days=30))
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    user = models.ForeignKey('AdvertisementUser', verbose_name='Пользователь', default=None,
                             null=True, on_delete=models.CASCADE, related_name='advertisement')
    heading = models.ForeignKey('AdvertisementHeading', verbose_name='Рубрика объявления', default=None,
                                null=True, on_delete=models.CASCADE,related_name='adver_heading')
    type = models.ForeignKey('AdvertisementType', verbose_name='Тип', default=None, null=True, on_delete=models.CASCADE,
                             related_name='adver_type')

class AdvertisementUser(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    email = models.CharField(verbose_name='Электронная почта', max_length=100)
    phone = models.CharField(verbose_name='Номер телефона', max_length=100)

    def __str__(self):
        return f'Имя пользователя: {self.name}, Электронная почта: {self.email}, Номер телефона: {self.phone}'

class AdvertisementType(models.Model):
    name = models.CharField(verbose_name='Тип объявления', max_length=100)

    def __str__(self):
        return self.name

class AdvertisementHeading(models.Model):
    name = models.CharField(verbose_name='Рубрика объявления', max_length=100)

    def __str__(self):
        return self.name