from django.db import models


class News(models.Model):
    name = models.CharField(verbose_name='Название объявления', max_length=100)
    description = models.TextField(verbose_name='Описание')
    create_date = models.DateField(verbose_name='Время создания', auto_now_add=True)
    update_date = models.DateField(verbose_name='Время редактирования', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активность объявления')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_date']

class Comment(models.Model):
    user_name = models.CharField(verbose_name='Имя пользователя', max_length=50)
    text = models.TextField(verbose_name='Комментарий')
    news_name = models.ForeignKey('News', verbose_name='Новость', default=None, null=True,  on_delete=models.CASCADE,
                                related_name='news')


