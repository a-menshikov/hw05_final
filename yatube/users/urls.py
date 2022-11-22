from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetDoneView)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('password_reset/',
         views.PasswordResetView.as_view(),
         name='password_reset_form'),
    path('reset/<slug:uidb64>/<slug:token>/',
         views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view
         (template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/complete/',
         PasswordResetCompleteView.as_view
         (template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/',
         views.PasswordChange.as_view(),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view
         (template_name='users/password_change_done.html'),
         name='password_change_done'),
]
