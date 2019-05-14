from django.contrib.auth.views import LogoutView
from django.urls import path

from wykop.accounts.views import (ConfirmTosView, RegisterView, UserDetailView,
                                  UserListView, UserLoginView, UserUpdateView)

app_name = 'accounts'

urlpatterns = [
    path('rejestracja', RegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('uzytkownicy', UserListView.as_view(), name='list'),
    path('profil/<int:pk>', UserDetailView.as_view(), name='profile'),
    path('edycja_profilu', UserUpdateView.as_view(), name='update'),
    path('regulamin', ConfirmTosView.as_view(), name='confirm_tos'),
]
