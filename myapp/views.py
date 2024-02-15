from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import auth


# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")




def my_view(request):
    response = HttpResponse()
    response.set_cookie('username', 'John Doe', max_age = 30 * 24* 60 * 60) #30 Days

    username = request.COOKIES.get('username', 'default_value_if_not_found')

    return response
