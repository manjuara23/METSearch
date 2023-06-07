from django.shortcuts import  render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from home.forms import UserSignupForm, AddBusRoute,AddBusStopage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import Bus,Bus_Route,Bus_Stopage

from .models import (
    Bus,
    Bus_Route,
    Bus_Stopage
)

# Create your views here.

def bus_details(request,pk):
    bus = get_object_or_404(Bus,pk=pk)
    
    return render(request,'home/bus_details.html',{
        'bus':bus,
    })


def home(request):
    return render(request, "home/home.html")

def index(request):
    buses = Bus.objects.all()
    
    return render(request, "home/index.html",{'buses':buses})

def allbus(request):
    
    buses = Bus.objects.all()
    
    return render(request, "home/buslist.html",{'buses':buses})

def addBuses(request):
    
    if(request.method=='POST'):
        print(request.POST['bus'])
        print(request.POST['route'])
        
        bus = Bus(bus_name=request.POST['bus'],
                  bus_id='0',route=request.POST['route'],
                  type=request.POST['type'],
                  station=request.POST['station'])
        bus.save()
        
        return redirect('Allbus')
    return render(request, "home/addBuses.html")
    # return render(request, "home/test.html")

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home/home.html')

def signup_view(request):
    # form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            # auto login
            username = request.POST['username']
            password = request.POST['password1']
            # email=request.POST.get['email']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
            else:
                print('User not found')
            
            return redirect('/')
        else:
            context = {
                'form':form
                }
            return render(request, 'home/signup.html', context)
    form = UserSignupForm()
    context = {
            'form':form
        }
    return render(request, 'home/signup.html', context)

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # we have to login
            login(request, user)
            
            return redirect('/')
        else:
            error = 'Username and password not matched!'
            context = {
                'error' : error
            }
            return render(request, 'home/login.html', context)
        
    
    return render(request, 'home/login.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'home/index.html')

def password_change_view(request):
    error = ""
    
    if request.method=='POST':
        username = request.user.username
        current_password = request.POST['password']
        
        user = authenticate(username=username, password = current_password)
        
        if user is not None:
            
            current_user = User.objects.get(username=username)
            
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            
            if password1 == password2:
                current_user.set_password(password1)
                current_user.save() 
            else:
                error = "New Password and Confirm Password do not match."
        else:
            error = "Current Password does not match."
            
    context ={
        'error' : error
    }  
    
    return render(request, 'password_change.html', context)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,'register.html',context) #context={"register_form":form})

def bus_route (request):
    if request.method == 'POST':
        form = AddBusRoute(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddBusRoute()
    return render(request, 'home/bus_route.html',{'form':form})


def bus_stopage (request):
    if request.method == 'POST':
        form = AddBusStopage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddBusStopage()
    return render(request, 'home/bus_stopage.html',{'form':form})
