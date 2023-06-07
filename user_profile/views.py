
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from .models import (
    Bus,
    Bus_Route,
    Bus_Stopage
)

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def index(request):
    return render(request, "home/index.html")

def allbus(request):
    return render(request, "home/buslist.html")

def addBuses(request):
    return render(request, "home/addBuses.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

