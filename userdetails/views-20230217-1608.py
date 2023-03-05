from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
# from users_details.forms import User_detailForm
from django.contrib import messages, auth
from .models import Userdetail
from django.http import HttpResponse
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exist !")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exist !")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,
                    email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
        return redirect('register')
    else:
        return render(request, 'user_details/register.html')
    
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in !')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')    
            return redirect('login')
    else:
        return render(request, 'user_details/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You have logged out !")
        return redirect('index')








