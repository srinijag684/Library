from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib import auth


# Create your views here.
'''def main(request):
    return render(request, 'myapp/index.html')'''

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    
    return render(request,'myapp/index.html')

def login_auth(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')'''
    
    username = request.POST.get('username', 'N')
    password = request.POST.get('password', '')

    #print(username, password) 

    #Hard-coded username and password for demonstration purposes
    if username == 'gourisrinijag' and password == 'Thelibrarypassword':
        return HttpResponseRedirect('/home/')

    #return messages.add_message(request, messages.INFO, 'Authentication failed. Please try again.')        
    return HttpResponse("Authentication failed. Please try again.")

def authenticated(request):
    return render(request, 'myapp/home.html')

def my_view(request):
    response = HttpResponse()
    response.set_cookie('username', 'John Doe', max_age = 30 * 24* 60 * 60) #30 Days

    username = request.COOKIES.get('username', 'default_value_if_not_found')

    return response