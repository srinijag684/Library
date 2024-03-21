from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('submit/', views.loginSubmit, name ='authenticate' ),
    path('logout/', views.logout, name='logout'),
    path('account/', views.account, name='account'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]