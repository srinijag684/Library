from django.urls import path
from .views import login_auth, login ,authenticated  #, main, 

urlpatterns = [
    #path('main/', main, name = 'main'),
    path('login/', login, name='login_page'),
    path('authenticate/', login_auth, name='login_auth'),
    path('home/', authenticated, name ='home'), 
]
