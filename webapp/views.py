from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_create(request):
    if request.user.is_authenticated is not None:
        return render(request, 'login.html')
    return redirect(to='home')
    

def login_store(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None: 
        login(request, user)
        return redirect(to='home')
    
    return redirect(to='login')

def user_logout(request):
    if request.user.is_authenticated is not None:
        logout(request)
        return redirect(to='home')
    return render(request, 'login.html')


#forms#
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm()

    return render(request, 'announcement_form.html', {'form': form})

def announcement_detail(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    return render(request, 'announcement_detail.html', {'announcement': announcement})

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcement_list.html', {'announcements': announcements})

def announcement_edit(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcement_form.html', {'form': form})
        
def announcement_delete(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    announcement.delete()
    return redirect('announcement_list')


 
def register_resident(request):
    form = ResidentForm
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resident_list')
        else:
            form = ResidentForm(request.POST)

    return render(request, 'resident_form.html', {'form': form})

def resident_detail(request, pk):
    resident = Resident.objects.get(pk=pk)
    return render(request, 'resident_detail.html', {'resident': resident})

def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'resident_list.html', {'residents': residents})

def resident_edit(request, pk):
    resident = Resident.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('resident_detail', pk=resident.pk)
    else:
        form = ResidentForm(instance=resident)
    return render(request, 'resident_edit.html', {'form': form, 'resident' :resident})

        
def resident_delete(request, pk):
    resident = Resident.objects.get(pk=pk)
    resident.delete()
    return redirect('resident_list')   