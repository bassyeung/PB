from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
#from users_details.forms import User_detailForm
from django.contrib import messages, auth
from .models import Userdetail
from django.http import HttpResponse
# Create your views here.

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
                messages.error(request, "Username already exist !")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exist !")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password,
                                                    email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    Cuser = User.objects.get(username=username, email=email)
                    userdetail = Userdetail.objects.create(
                        user_id=Cuser.id, status="active")
                    userdetail.save()
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

def info_update(request):
    if request.method =='POST':
        # form = User_detailForm(request.POST)
        print("adesdede")
        # if form.is_valid():
        print("gogo")
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        ucountry = request.POST['country']
        email = request.POST['email']
        phone = request.POST['phone']
        credit = request.POST['credit_card']
        ucountry = request.POST['country']
        oldpass = request.POST['oldpass']
        if User.objects.get(username=username).check_password(oldpass):
            print('correct')
            print(password1)
            if password1 != "":
                print('yessss')
                if password1 == password2:
                    print("yes1")
                    Userdetail.objects.filter(id = request.user.id).update( country = ucountry, phone_num = phone, credit_card = credit)
                    User.objects.filter(id = request.user.id).update(username=username, email=email, password = password1)
                    return redirect('account')
                else:
                    print("warning")
                    messages.warning(request, "password does not match")
                    return redirect('info_update')
            else:
                print('?????')
                print("yes2")
                Userdetail.objects.filter(id = request.user.id).update( country = ucountry, phone_num = phone, credit_card = credit)
                User.objects.filter(id = request.user.id).update(username=username, email=email)
                return redirect('account')
        else:
            messages.warning(request, "password incorrect")
            return redirect('info_update')
    #form = User_detailForm()
    return render(request, 'user_details/info_update.html')
    
    
        

def account(request):
    # user_detail = get_object_or_404(User_detail,pk=user_detail_id)
    # context = {
    #     'udetail': user_detail,
    # }
    # # return render(request, 'users_details/account.html', context)
    # user_contacts = User.objects.filter(pk=request.user.id)
    # context = {
    #     'udetail': user_contacts
    # }, context
    # print(User_detail.address)
    # print(User_detail.credit_card)
    return render(request, 'user_details/account.html')