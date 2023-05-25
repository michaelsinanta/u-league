from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from uuid import uuid4;
from django.views.decorators.csrf import csrf_exempt

def show_pembuatan_pertandingan(request):
    username = request.session.get('info', {}).get('username', None)    

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)
    
    
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT T.id_pertandingan AS id_pertandingan, string_agg(T.nama_tim, ' vs ') AS team_names
            FROM PERTANDINGAN AS P
            JOIN STADIUM AS S ON P.stadium = S.id_stadium
            JOIN TIM_PERTANDINGAN AS T ON T.id_pertandingan = P.id_pertandingan
            GROUP BY T.id_pertandingan;
        """)
        pertandingan = dict_fetch_all(cursor)
        grupA = []
        grupA.append(pertandingan[0:4])
        grupB = []
        grupB.append(pertandingan[4:8])
        grupC = []
        grupC.append(pertandingan[8:12])
        grupD = []
        grupD.append(pertandingan[12:16])
        context['grupA'] = grupA[0]
        context['grupB'] = grupB[0]
        context['grupC'] = grupC[0]
        context['grupD'] = grupD[0]

        cursor.execute(f"""
            SELECT nama, id_stadium
            FROM STADIUM;
        """)
        stadiums = dict_fetch_all(cursor)
        context['stadiums'] = stadiums

    return render(request, 'pembuatan_pertandingan.html', context)
    
    
def update_pertandingan(request, id_pertandingan):
    if request.method == 'POST':
        wasit_utama = request.POST.get('wasit_utama')
        wasit_pembantu1 = request.POST.get('wasit_pembantu1')
        wasit_pembantu2 = request.POST.get('wasit_pembantu2')
        wasit_cadangan = request.POST.get('wasit_cadangan')
        nama_team1 = request.POST.get('nama_team1')
        nama_team2 = request.POST.get('nama_team2')
        id_pertandingan = request.POST.get('id_pertandingan')

    with connection.cursor() as cursor:
        cursor.execute(f"""
            UPDATE WASIT_BERTUGAS SET posisi_wasit = 'wasit utama' WHERE '{wasit_utama}' = id_wasit;
            UPDATE WASIT_BERTUGAS SET posisi_wasit = 'hakim garis' WHERE '{wasit_pembantu1}' = id_wasit;
            UPDATE WASIT_BERTUGAS SET posisi_wasit = 'hakim garis' WHERE '{wasit_pembantu2}' = id_wasit;
            UPDATE WASIT_BERTUGAS SET posisi_wasit = 'wasit cadangan' WHERE '{wasit_cadangan}' = id_wasit;
            UPDATE TIM_PERTANDINGAN SET nama_tim = '{nama_team1}' WHERE '{id_pertandingan}' = id_pertandingan;
            UPDATE TIM_PERTANDINGAN SET nama_tim = '{nama_team2}' WHERE '{id_pertandingan}' = id_pertandingan;
        """)
    

def delete_pertandingan(request, id_pertandingan):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            DELETE FROM PERTANDINGAN
            WHERE id_pertandingan='{id_pertandingan}';
        ''')

        return redirect('landing_page.html')

def show_list_waktu_stadium(request):
    username = request.session.get('info', {}).get('username', None) 

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)
    
    stadium_name = request.GET.get('stadium_name')
    id_stadium = request.GET.get('id_stadium')
    date = request.GET.get('date')

    context = {
        'stadium_name': stadium_name,
        'id_stadium' : id_stadium,
        'date' : date,
        'user': {'role': f'{role}'}
    }

    return render(request, 'list_waktu_stadium.html', context)


def buat_pertandingan(request):
    username = request.session.get('info', {}).get('username', None) 

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    

    if role != "Panitia":
        return render(request, 'landing_page.html', context)

    id_pertandingan = uuid4
    id_stadium = request.GET.get('id_stadium')
    start_hours = request.GET.get('start_hours')
    end_hours = request.GET.get('end_hours')
    date = request.GET.get('date')

    context = {
        'user': {'role': f'{role}'},
        'start_hours': start_hours,
        'end_hours': end_hours,
        'date': date,
        'id_stadium':id_stadium,
        'id_pertandingan':id_pertandingan
    } 
    
    with connection.cursor() as cursor:
        cursor.execute(f"""
        SELECT nama_depan, nama_belakang, id_wasit
        FROM NON_PEMAIN, WASIT
        WHERE id = id_wasit;
        """)
        wasit = dict_fetch_all(cursor)
        context['wasit'] = wasit

        cursor.execute(f"""
            SELECT DISTINCT T.nama_tim
            FROM TIM T
            JOIN TIM_MANAJER M ON T.nama_tim = M.nama_tim
            JOIN PEMINJAMAN P ON M.id_manajer = P.id_manajer
            WHERE '{id_stadium}' = P.id_stadium;
            """)
        tim = dict_fetch_all(cursor)
        context['tim'] = tim

    
    return render(request, 'buat_pertandingan_antar_2tim.html', context)

@csrf_exempt
def add_pertandingan(request):
    if request.method == 'POST':
        wasit_utama = request.POST.get('wasitUtama')
        wasit_pembantu1 = request.POST.get('wasitPembantu1')
        wasit_pembantu2 = request.POST.get('wasitPembantu2')
        wasit_cadangan = request.POST.get('wasitCadangan')
        nama_team1 = request.POST.get('team1')
        nama_team2 = request.POST.get('team2')
        start_hours = request.POST.get('start_hours')
        end_hours = request.POST.get('end_hours')
        id_stadium = request.POST.get('id_stadium')
        id_pertandingan = request.POST.get('id_pertandingan')
        date = request.POST.get('date')

    with connection.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO PERTANDINGAN(id_pertandingan, start_datetime, end_datetime, stadium) VALUES
            ('{id_pertandingan}','{date + " " + start_hours}','{date + " " + end_hours}','{id_stadium}');
            INSERT INTO WASIT_BERTUGAS(id_wasit, id_pertandingan, posisi_wasit) VALUES
            ('{wasit_utama}', '{id_pertandingan}', 'wasit utama');
            INSERT INTO WASIT_BERTUGAS(id_wasit, id_pertandingan, posisi_wasit) VALUES
            ('{wasit_pembantu1}', '{id_pertandingan}', 'hakim garis');
            INSERT INTO WASIT_BERTUGAS(id_wasit, id_pertandingan, posisi_wasit) VALUES
            ('{wasit_pembantu2}', '{id_pertandingan}', 'hakim garis');
            INSERT INTO WASIT_BERTUGAS(id_wasit, id_pertandingan, posisi_wasit) VALUES
            ('{wasit_cadangan}', '{id_pertandingan}', 'wasit cadangan');
            INSERT INTO TIM_PERTANDINGAN(nama_tim, id_pertandingan, skor) VALUES
            ('{nama_team1}', '{id_pertandingan}', 0);
            INSERT INTO TIM_PERTANDINGAN(nama_tim, id_pertandingan, skor) VALUES
            ('{nama_team2}', '{id_pertandingan}', 0);
        """)
        return JsonResponse({"message": "Pembuatan pertandingan sukses", "status": 200})
