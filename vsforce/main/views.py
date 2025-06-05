from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Service, StaffMember
from .forms import ContactForm

# Home page view
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

# About page view
def about(request):
    return render(request, 'about.html')

# Services page view with search
def services(request):
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(name__icontains=query)
    else:
        services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

# Contact page view with form handling
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Reloads contact page after submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Staff page view with search
def staff(request):
    query = request.GET.get('q')
    if query:
        staff_members = StaffMember.objects.filter(name__icontains=query) | StaffMember.objects.filter(role__icontains=query)
    else:
        staff_members = StaffMember.objects.all()
    return render(request, 'staff.html', {'staff_members': staff_members})

# Service detail view
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})

# User signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
