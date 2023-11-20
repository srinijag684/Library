from django.urls import path
from .views import login, login_auth, authenticated

urlpatterns = [
    path('login/', login, name='login_page'),
    path('authenticate/', login_auth, name='login_auth'),
    path('home/', authenticated, name ='home'), 
]
