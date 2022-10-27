from django.urls import path

from app_users.views import restore_password, AnotherLoginView, AnotherLogoutView

urlpatterns = [
    path('restore_password/', restore_password, name='restore_password'),
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
]
