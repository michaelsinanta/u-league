from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import render
from datetime import datetime


def manage_pertanding(request) :
    
    context = process_username(request)

    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT T.id_pertandingan AS id_pertandingan, string_agg(T.nama_tim, ' vs ') AS team_names, P.start_datetime
                FROM PERTANDINGAN AS P
                JOIN TIM_PERTANDINGAN AS T ON T.id_pertandingan = P.id_pertandingan
                GROUP BY P.start_datetime, T.id_pertandingan;
            """)
        list_pertandingan = dict_fetch_all(cursor)
        context['available_pertandingan'] = len(list_pertandingan) > 0
        grupA = []
        grupA.append(list_pertandingan[0:4])
        grupB = []
        grupB.append(list_pertandingan[4:8])
        grupC = []
        grupC.append(list_pertandingan[8:12])
        grupD = []
        grupD.append(list_pertandingan[12:16])
        context['grupA'] = grupA[0]
        context['grupB'] = grupB[0]
        context['grupC'] = grupC[0]
        context['grupD'] = grupD[0]
        context['available_A'] = len(grupA) > 0
        context['available_B'] = len(grupB) > 0
        context['available_C'] = len(grupC) > 0
        context['available_D'] = len(grupD) > 0

    return render(request, 'manage_pertandingan.html', context)

def list_pertandingan_grup(request):
    context = process_username(request)
    return render(request, 'list_pertandingan_grup.html', context)

def peristiwa(request, nama_tim):
    context = process_username(request)
    # context['nama_tim'] = nama_tim

    return render(request, 'peristiwa.html', context) 
    

def process_username(request):
    username = request.session['info'].get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 

    role = get_user_role(username)
    context = {
        'user': {
            'role': f'{role}',
        }
    }
    if(role != "Panitia") :
        return render(request, 'landing_page.html', context)
    return context