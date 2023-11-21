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
        if username == 'user' and password == '1234':
            return HttpResponseRedirect('/home/')

    #return messages.add_message(request, messages.INFO, 'Authentication failed. Please try again.')        
    return HttpResponse("Authentication failed. Please try again.")

def authenticated(request):
    return render(request, 'myapp/home.html')
