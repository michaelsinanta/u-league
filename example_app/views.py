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
def pembuatan_pertandingan(request):
    return render(request, 'pembuatan_pertandingan.html')

def list_waktu_stadium(request):
    return render(request, 'list_waktu_stadium.html')

def buat_pertandingan_antar_2tim(request):
    return render(request, 'buat_pertandingan_antar_2tim.html')

def list_pertandingan(request):
    return render(request, 'list_pertandingan.html')

def history_rapat(request):
    return render(request, 'history_rapat.html')
