from django.shortcuts import render, get_object_or_404, redirect
from .models import Temple, Pooja, Booking
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import TempleForm, PoojaForm
from django.utils.crypto import get_random_string

def is_staff(user):
    return user.is_staff

def home(request):
    temples = Temple.objects.all()
    return render(request, "index.html", {"temples": temples})

def pooja_list(request):
    poojas = Pooja.objects.filter(active=True)
    return render(request, "pooja.html", {"poojas": poojas})

def book_pooja(request, id):
    pooja = get_object_or_404(Pooja, id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        nakshatra = request.POST.get("nakshatra")
        booking = Booking.objects.create(
            user=request.user if request.user.is_authenticated else None,
            devotee_name=name,
            temple=pooja.temple,
            pooja=pooja,
            date=date,
            nakshatra=nakshatra,
            payment_status='PENDING'
        )
        return redirect('payment_selection', booking_id=booking.id)
    return render(request, "booking.html", {"pooja": pooja})

def payment_selection(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "payment.html", {"booking": booking})

def process_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    # Simulate processing (In real app, logic would go here)
    booking.payment_status = 'SUCCESS'
    booking.transaction_id = 'DS-' + get_random_string(12).upper()
    booking.save()
    return redirect('payment_success', booking_id=booking.id)

def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "payment_success.html", {"booking": booking})

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "dashboard.html", {"bookings": bookings})

# Institutional Administration Views
@user_passes_test(is_staff)
def admin_dashboard(request):
    if request.user.is_superuser:
        temples = Temple.objects.all()
        poojas = Pooja.objects.all()
        bookings = Booking.objects.all()
    else:
        temples = Temple.objects.filter(admin_user=request.user)
        poojas = Pooja.objects.filter(temple__in=temples)
        bookings = Booking.objects.filter(temple__in=temples)
    
    stats = {
        'temples_count': temples.count(),
        'poojas_count': poojas.count(),
        'bookings_count': bookings.count(),
        'recent_bookings': bookings.order_by('-created_at')[:5]
    }
    return render(request, "admin_portal.html", {"stats": stats})

@user_passes_test(is_staff)
def manage_temples(request):
    if request.user.is_superuser:
        temples = Temple.objects.all()
    else:
        temples = Temple.objects.filter(admin_user=request.user)
        
    if request.method == "POST":
        form = TempleForm(request.POST, request.FILES)
        if form.is_valid():
            temple = form.save(commit=False)
            if not request.user.is_superuser:
                temple.admin_user = request.user
            temple.save()
            return redirect('manage_temples')
    else:
        form = TempleForm()
    return render(request, "manage_temples.html", {"temples": temples, "form": form})

@user_passes_test(is_staff)
def edit_temple(request, id):
    if request.user.is_superuser:
        temple = get_object_or_404(Temple, id=id)
    else:
        temple = get_object_or_404(Temple, id=id, admin_user=request.user)
        
    if request.method == "POST":
        form = TempleForm(request.POST, request.FILES, instance=temple)
        if form.is_valid():
            form.save()
            return redirect('manage_temples')
    else:
        form = TempleForm(instance=temple)
    
    if request.user.is_superuser:
        all_temples = Temple.objects.all()
    else:
        all_temples = Temple.objects.filter(admin_user=request.user)
        
    return render(request, "manage_temples.html", {"temples": all_temples, "form": form, "edit_mode": True, "edit_id": id})

@user_passes_test(is_staff)
def delete_temple(request, id):
    if request.user.is_superuser:
        temple = get_object_or_404(Temple, id=id)
    else:
        temple = get_object_or_404(Temple, id=id, admin_user=request.user)
    temple.delete()
    return redirect('manage_temples')

@user_passes_test(is_staff)
def manage_poojas(request):
    if request.user.is_superuser:
        poojas = Pooja.objects.all()
        temples = Temple.objects.all()
    else:
        temples = Temple.objects.filter(admin_user=request.user)
        poojas = Pooja.objects.filter(temple__in=temples)
        
    if request.method == "POST":
        form = PoojaForm(request.POST, request.FILES)
        if form.is_valid():
            pooja = form.save(commit=False)
            # Ensure the temple belongs to the admin
            if not request.user.is_superuser and pooja.temple not in temples:
                return redirect('manage_poojas')
            pooja.save()
            return redirect('manage_poojas')
    else:
        form = PoojaForm()
        # Filter temple choices in form if not superuser
        if not request.user.is_superuser:
            form.fields['temple'].queryset = temples
            
    return render(request, "manage_poojas.html", {"poojas": poojas, "form": form})

@user_passes_test(is_staff)
def edit_pooja(request, id):
    if request.user.is_superuser:
        pooja = get_object_or_404(Pooja, id=id)
        temples = Temple.objects.all()
    else:
        temples = Temple.objects.filter(admin_user=request.user)
        pooja = get_object_or_404(Pooja, id=id, temple__in=temples)
        
    if request.method == "POST":
        form = PoojaForm(request.POST, request.FILES, instance=pooja)
        if form.is_valid():
            pooja_obj = form.save(commit=False)
            if not request.user.is_superuser and pooja_obj.temple not in temples:
                return redirect('manage_poojas')
            pooja_obj.save()
            return redirect('manage_poojas')
    else:
        form = PoojaForm(instance=pooja)
        if not request.user.is_superuser:
            form.fields['temple'].queryset = temples

    if request.user.is_superuser:
        all_poojas = Pooja.objects.all()
    else:
        all_poojas = Pooja.objects.filter(temple__in=temples)
        
    return render(request, "manage_poojas.html", {"poojas": all_poojas, "form": form, "edit_mode": True, "edit_id": id})

@user_passes_test(is_staff)
def delete_pooja(request, id):
    if request.user.is_superuser:
        pooja = get_object_or_404(Pooja, id=id)
    else:
        temples = Temple.objects.filter(admin_user=request.user)
        pooja = get_object_or_404(Pooja, id=id, temple__in=temples)
    pooja.delete()
    return redirect('manage_poojas')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard' if user.is_staff else '/')
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create_user(username=username, password=password)
        return redirect('/login')
    return render(request, "register.html")

def user_logout(request):
    logout(request)
    return redirect('/')