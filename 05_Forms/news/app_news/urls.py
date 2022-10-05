from django.urls import path
from . import views

urlpatterns = [
    path("news_list", views.NewsView.as_view(), name='news_list'),
    path("news/create", views.CreateNewsView.as_view(), name='create'),
    path("news/update<int:pk>", views.UpdateNewsView.as_view(), name='update'),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name='detail'),
    path("comment/create<int:news_id>", views.NewsDetailView.as_view(), name='create_comment'),
    path("login/", views.ViewLogin.as_view(), name='login'),
    path("logout/", views.ViewLogout.as_view(), name='logout'),
    path("main/", views.Main.as_view(), name='main'),
]