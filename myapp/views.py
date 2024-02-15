from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    return render(request,'/Users/gourisrinijag/theLibrary/myapp/templates/registration/login.html')

def loginSubmit(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    
    username = request.POST.get('username','N')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        return render(request,'templates/registration/login.html')
        
def logout(request):
    auth.logout(request)
    return redirect(login)



def my_view(request):
    response = HttpResponse()
    response.set_cookie('username', 'John Doe', max_age = 30 * 24* 60 * 60) #30 Days

    username = request.COOKIES.get('username', 'default_value_if_not_found')

    return response
