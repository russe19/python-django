from django.core.management.base import BaseCommand
from advertisements_app.models import Advertisement, AdvertisementUser, AdvertisementType, AdvertisementHeading
from itertools import count
import random
import string
from django.utils import timezone

class Command(BaseCommand):
    help = 'The Zen of Python'


    def handle(self, *args, **options):
        number = '0123456789'
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        a = AdvertisementHeading.objects.create(name='Авто')
        a.save()
        a = AdvertisementHeading.objects.create(name='Недвижимость')
        a.save()
        a = AdvertisementHeading.objects.create(name='Работа')
        a.save()
        a = AdvertisementType.objects.create(name='Архив')
        a.save()
        a = AdvertisementType.objects.create(name='Черновик')
        a.save()
        a = AdvertisementType.objects.create(name='Опубликовано')
        a.save()
        for i in range(10):
            a = AdvertisementUser.objects.create(name=''.join(random.choice(alpha) for i in range(7)),
                                             email=''.join(random.choice(alpha) for i in range(6)) + '@mail.ru',
                                             phone = ''.join(random.choice(number) for i in range(11)))
            a.save()
        for i in range(20):
            us = AdvertisementUser.objects.get(id=random.randint(1, 10))
            us.save()
            ty = AdvertisementType.objects.get(id=random.randint(1, 3))
            ty.save()
            h = AdvertisementHeading.objects.get(id=random.randint(1, 3))
            h.save()
            a = Advertisement.objects.create(title=f'Объявление {i}', description=f'Описание объявления {i}',
                                             price = random.randint(1000, 100000),
                                             user = us, type = ty, heading = h)
            a.save()
        print(Advertisement.objects.all())