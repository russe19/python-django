from django.urls import path
from app_media import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.regist_view, name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('main/', views.Main.as_view(), name='main'),
    path('entres/', views.EntryList.as_view(), name='entres'),
    path('upload_entry/', views.upload_entry, name='upload_entry'),
    path('entry_detail<int:pk>/', views.EntryDetail.as_view(), name='entry_detail'),
    path('upload_file/', views.upload_file, name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)