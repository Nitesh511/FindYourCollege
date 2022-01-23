from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login', views.login_user),
    path('register', views.register_user),
    path('logout' , views.logout_user),
    path('password_change_user', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_user.html')),
    path('password_change_done_user', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_done_user.html'), name='password_change_done'),
    path('seecollege',views.back)
]

