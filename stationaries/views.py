from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from .models import Stationaries
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import login as auth_login
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from .import views




# Create your views here.

def home(request):
    #return HttpResponse("Hello Im working")
    return render(request, "stationaries/login.html")

def signup(request):
      return render(request, "stationaries/signup.html")


    ## myuser.save()
        
       # messages.success(request, "Your account has been successfully created.Please Log in.")
       # return redirect("stationaries/login.html")
      #  return redirect("/signup.html")

#def user(request):
    #if user is not None:
       # login(request, user)
       # fname = user.first_name
        #return render( request,"stationaries/login.html", {'fname': fname})
    
def login(request):
         return render(request, "stationaries/login.html")
    #if request.method == "POST":
       # username = request.POST['username']
       # pass1 =request.POST['pass1']
        
       # user = authenticate(username=username, password=pass1)
        #return render(request, "stationaries/index.html")
        
        #else:
             # messages.error(request, "Your account deosn't match")
             # return redirect('stationaries/login.html')
    
    #return render(request, "stationaries/index.html")

def logo(request):
    return render(request, "stationaries/logo.html")

def aboutus(request):
    return render(request, "stationaries/aboutus.html")

def index(request):
    return render(request, "stationaries/index.html")

#def our_products(request):
    #return render(request, "our_products.html")

    
     