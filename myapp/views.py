from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'myapp/index.html')

def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password) 

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