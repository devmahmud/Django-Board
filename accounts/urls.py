from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('user/profile/', views.UserUpdateView.as_view(), name='profile'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
    ), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html',
    ), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
         template_name='registration/password_reset.html',
         email_template_name='registration/password_reset_email.html',
         subject_template_name='registration/password_reset_subject.txt'),
         name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

]
