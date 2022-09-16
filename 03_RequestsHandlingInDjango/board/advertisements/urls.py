from django.urls import path
from . import views

urlpatterns = [
    path("advertisements", views.Regions.as_view()),
    path("contacts", views.Contacts.as_view()),
    path("about", views.About.as_view(), name='about'),
    path("", views.Main.as_view()),
]
