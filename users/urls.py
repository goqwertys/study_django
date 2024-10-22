from sys import meta_path
from tkinter.font import names

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserProfileUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path(
        'logout/', LogoutView.as_view(
            # http_method_names=["post", "get", "options"],
            next_page='/catalog/'),
         name='logout'
    ),
    path('register', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit')
]
