from django.shortcuts import render,redirect
from .models import employees
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        age=request.POST['age']
        address=request.POST['address']
        emailexists=employees.objects.filter(Email=email)
        if emailexists:
            messages.error(request,'Email id already registered')
        else:
            employees(Name=name,Email=email,Age=age,Password=password,Address=address).save()
            return redirect('index')
    return render(request,"register.html")

