# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from datetime import date
from website.models import *
from django.contrib.auth import login as auth_login, authenticate, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import auth,messages
from .forms import PasswordForm
from .models import Reservation, User
from datetime import datetime
from django.shortcuts import HttpResponseRedirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def index(request): 
    success = [];
    if request.method == 'POST': # If the form has been submitted...
        #form = ContactForm(request.POST)
        reserve = request.POST
        #print(request.POST)
        date_in = reserve.get('date-in')#[""]
        #print(date_in)
        if date_in=='':
            date_in = date.today()

        date_out = reserve.get("date-out")
        if date_out =='':
            date_out = date.today()
        
        guest = reserve.get("guest")  
        if guest =='':
            guest = 1;     
        room = reserve.get("room")
        if room =='':
            room = 1; 
        email = reserve.get("email")
        phone = reserve.get("phone")
        if email == '' and phone == '':
            success.append(23)
        else:
            Reservation.objects.create(CheckIn=str(date_in), CheckOut=str(date_out), NumeberOfGuest=str(guest), NumeberOfRooms=str(room), Email=str(email), Phone =str(phone))
        print(date_in,date_out,email,phone,guest,room)  
    return render(request, 'index.html',context={'success': success})

def about_us(request): 
    return render(request, 'about-us.html')

def rooms(request): 
    return render(request, 'rooms.html')

def whattosee(request): 
    return render(request, 'blog.html')

def contact(request): 
    return render(request, 'contact.html')

@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            is_old_and_new_similar=request.user.check_password(form.cleaned_data['new_password1'])
            if is_old_and_new_similar==False: 
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request,'Your password was successfully updated!')
                form = PasswordForm(request.user)           
            else:
                messages.error(request,'New password must not similar to old')          
        else:
            messages.error(request,'Data is Invalid!')
    else:
        messages.info(request,"Please Set Valid Data As Stated!")  
        form = PasswordForm(request.user)
    return render(request, 'change_password.html', {'form': form })

@login_required(login_url="login")
def dashboard(request): 
    return render(request, 'admin_index.html', context={'files':Reservation.objects.all()})

@login_required(login_url="login")
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

def user_login(request):
    if request.GET:
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('dashboard')
        
    return render(request, "login.html")