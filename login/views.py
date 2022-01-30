from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Doctor



def index(request):
    return render(request, 'login/index.html')
def register(request):    
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name','')
        password = request.POST.get('password','')
        print(first_name, 'Name')
        global ark, fit 
        ark = user_name
        fit = first_name
        #customer = Customer(user_name = user_name, password = password)
        #customer.save()

        doctor = Doctor(first_name = first_name, last_name = last_name, user_name = user_name, password = password)
        doctor.save()
    return render(request, 'login/register.html')        
def home(request):
    print('login-request')
    return render(request, 'login/home.html', { 'email': ark, 'name': fit })
