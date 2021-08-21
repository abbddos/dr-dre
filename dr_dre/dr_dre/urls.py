"""dr_dre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from login import views as login_views
from home import views as home_views
from dre_admin import views as dre_views
from dre_jobs import views as job_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('home/', include('home.urls')),
    path('dre_admin/', include('dre_admin.urls')),
    path('dre_jobs/', include('dre_jobs.urls')),
    path('profile/<uid>', dre_views.profile, name = 'profile'),
    path('change_password/<uid>', dre_views.change_password, name = 'change_password'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login/logout.html'), name = 'logout'), 
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'login/reset_password.html'), name = 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'login/password_reset_sent.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'login/password_reset_form.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'login/password_reset_done.html'), name = 'password_reset_complete')
]
