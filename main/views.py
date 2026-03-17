from django.shortcuts import render
from .models import Temple, Pooja, Booking
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    temples = Temple.objects.all()
    return render(request,"index.html",{"temples":temples})


def pooja_list(request):
    poojas = Pooja.objects.all()
    return render(request, "pooja.html", {"poojas": poojas})


def book_pooja(request, id):

    pooja = Pooja.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")

        Booking.objects.create(
            user_name=name,
            pooja=pooja,
            date=date
        )

        return redirect('/')

    return render(request,"booking.html",{"pooja":pooja})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
    
    return render(request,"login.html")

def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username,password=password)

        return redirect('/login')

    return render(request,"register.html")