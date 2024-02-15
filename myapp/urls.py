from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    #path('', views.loginSubmit, name ='authenticate' )
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
]