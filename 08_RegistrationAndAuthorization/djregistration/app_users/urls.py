from django.urls import path
from . import views

urlpatterns = [
    path('main', views.MainView.as_view(), name='main'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.register_view, name='register'),
    path("news_list", views.NewsView.as_view(), name='news_list'),
    path("news/create", views.CreateNewsView.as_view(), name='create'),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name='detail'),
    path("comment/create<int:news_id>", views.NewsDetailView.as_view(), name='create_comment'),
    path("users", views.UserVerView.as_view(), name='users')
]

