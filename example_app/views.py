from django.shortcuts import render
from example_app.utils import get_user_role

def index(request):
    username = request.session['info'].get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 

    role = get_user_role(username)
    context = {
        'user': {
            'role': f'{role}',
        },
        'username':username
    }

    return render(request, 'index.html', context)

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

def pilih_stadium(request):
    return render(request, 'pilih_stadium.html')

def list_waktu_stadium(request):
    return render(request, 'list_waktu_stadium.html')

def buat_pertandingan_antar_2tim(request):
    return render(request, 'buat_pertandingan_antar_2tim.html')

def list_pertandingan(request):
    return render(request, 'list_pertandingan.html')

def pilih_pertandingan(request):
    return render(request, 'pilih_pertandingan.html')

def history_rapat(request):
    return render(request, 'history_rapat.html')

def pengguna(request):
    return render(request, 'pengguna.html')

def regis1(request):
    return render(request, 'form_regis_manajer.html')

def regis2(request):
    return render(request, 'form_regis_panitia.html')

def mulai_rapat(request):
    return render(request, 'mulai_rapat.html')

def rapat(request):
    return render(request, 'rapat.html')

def mulai_pertandingan(request):
    return render(request, 'mulai_pertandingan.html')

def peristiwa(request):
    return render(request, 'peristiwa.html')

def register_tim(request):
    username = request.session['info'].get('username')

    role = get_user_role(username)
    context = {
        'user': {
            'role': f'{role}',
        }
    }
    return render(request, 'register_tim.html', context)

def my_team(request):
    return render(request, 'my_team.html')
