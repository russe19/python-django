from django.urls import path
from . import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path("advertisement1", views.advertisement_1, name='advertisement_1'),
    path("advertisement2", views.advertisement_2, name='advertisement_2'),
    path("advertisement3", views.advertisement_3, name='advertisement_3'),
    path("advertisement4", views.advertisement_4, name='advertisement_4'),
    path("advertisement5", views.advertisement_5, name='advertisement_5')
]