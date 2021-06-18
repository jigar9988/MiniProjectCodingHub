from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from CodingHub.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout


def index(request):
    return render(request, 'index.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def htuto(request):
    return render(request, 'htuto.html')
    
def csstuto(request):
    return render(request, 'csstuto.html')
    
def jstuto(request):
    return render(request, 'jstuto.html')
    
def java(request):
    return render(request, 'java.html')
    
def cpp(request):
    return render(request, 'cpp.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                    desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Form Succesfully Submitted.')
    return render(request, 'contact.html')

    # return HttpResponse("Home Page")
# Create your views here.


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameter
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('index')

        # create the user
        myuser = User.objects.create_user(username, useremail, pass1)
        myuser.save()
        messages.success(request, 'Your Account Has been Craeted successfully')
        return redirect('index')

    else:
        return HttpResponse('404 Not Found')


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")

    return HttpResponse("login")



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')