from django.urls import path, include
from app_users.views import example, greatings

urlpatterns = [
    path('example/', example, name='example'),
    path('greatings/', greatings, name='greatings'),
]