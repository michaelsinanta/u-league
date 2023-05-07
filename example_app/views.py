from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def login(request) :
    return render(request, 'login.html')

def manage_pertanding(request) :
    return render(request, 'manage_pertandingan.html')

def dashboardManajer(request):
    return render(request, 'dashboardManajer.html')

def dashboardPenonton(request):
    return render(request, 'dashboardPenonton.html')

def dashboardPanitia(request):
    return render(request, 'dashboardPanitia.html')
