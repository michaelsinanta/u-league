from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard_manajer(request):
    return render(request, 'dashboard_manajer.html')

def dashboard_penonton(request):
    return render(request, 'dashboard_penonton.html')

def dashboard_panitia(request):
    return render(request, 'dashboard_panitia.html')

def beli_tiket(request):
    return render(request, 'beli_tiket.html')

def list_waktu_stadium(request):
    return render(request, 'list_waktu_stadium.html')

def pilih_pertandingan(request):
    return render(request, 'pilih_pertandingan.html')