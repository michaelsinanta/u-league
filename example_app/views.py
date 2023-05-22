from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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
