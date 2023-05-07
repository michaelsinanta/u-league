from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboardManajer(request):
    return render(request, 'dashboardManajer.html')

def dashboardPenonton(request):
    return render(request, 'dashboardPenonton.html')

def dashboardPanitia(request):
    return render(request, 'dashboardPanitia.html')