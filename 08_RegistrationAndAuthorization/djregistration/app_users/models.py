from django.db import models
from django.contrib.auth.models import User, Group


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    verification = models.BooleanField(default=False, verbose_name='Верификация')
    count_news = models.IntegerField(default=0, verbose_name='Кол-во опубликованных новостей')


class News(models.Model):
    name = models.CharField(verbose_name='Название объявления', max_length=100)
    description = models.TextField(verbose_name='Описание')
    create_date = models.DateField(verbose_name='Время создания', auto_now_add=True)
    update_date = models.DateField(verbose_name='Время редактирования', auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='Активность объявления')
    tag = models.CharField(verbose_name='Тэг', default=None, null=True, max_length=50)

    def __str__(self):
        return f'Новость: {self.name}, Дата публикации: {self.create_date}, Активность: {self.is_active}'

    class Meta:
        ordering = ['tag', 'create_date']


class Comment(models.Model):
    user_name = models.CharField(verbose_name='Имя пользователя', default=None, null=True, max_length=50)
    text = models.TextField(verbose_name='Комментарий')
    news_name = models.ForeignKey('News', verbose_name='Новость', default=None, null=True, on_delete=models.CASCADE,
                                  related_name='news')
    user = models.ForeignKey(User, verbose_name='Пользователь', default=None, null=True, on_delete=models.CASCADE,
                             related_name='user')

    def __str__(self):
        if len(self.text) > 15:
            text = self.text[:15]+'...'
        else:
            text = self.text
        return f'Имя пользователя: {self.user_name}, Комментарий: {text}'






