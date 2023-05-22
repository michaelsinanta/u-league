from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dashboard_manajer(request):
    return render(request, 'dashboard_manajer.html')
  
def landing_page(request):
    return render(request, 'landing_page.html')

def login(request) :
    return render(request, 'login.html')

def manage_pertanding(request) :
    return render(request, 'manage_pertandingan.html')

def pembuatan_pertandingan(request):
    return render(request, 'pembuatan_pertandingan.html')

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

def history_rapat(request):
    return render(request, 'history_rapat.html')

def pengguna(request):
    return render(request, 'pengguna.html')

def regis1(request):
    return render(request, 'form_regis1.html')

def regis2(request):
    return render(request, 'form_regis2.html')

def mulai_rapat(request):
    return render(request, 'mulai_rapat.html')

def rapat(request):
    return render(request, 'rapat.html')

def mulai_pertandingan(request):
    return render(request, 'mulai_pertandingan.html')

def peristiwa(request):
    return render(request, 'peristiwa.html')

def register_tim(request):
    return render(request, 'register_tim.html')

def peminjaman_stadium(request):
    return render(request, 'peminjaman_stadium.html')

def my_team(request):
    return render(request, 'my_team.html')
