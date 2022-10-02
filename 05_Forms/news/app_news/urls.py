from django.urls import path
from . import views

urlpatterns = [
    path("news_list", views.NewsView.as_view(), name='news_list'),
    path("news/create", views.CreateView.as_view(), name='create'),
    path("news/created_news", views.CreateView.as_view(), name='created_news'),
    path("news/update<int:profile_id>", views.UpdateView.as_view(), name='update'),
    path("news/updated_news<int:profile_id>", views.UpdateView.as_view(), name='updated_news'),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name='detail'),
    path("comment/create<int:news_id>", views.NewsDetailView.as_view(), name='create_comment'),
]