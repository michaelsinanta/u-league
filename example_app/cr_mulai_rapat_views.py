from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime, timedelta
import random

def mulai_rapat(request):
    username = request.session.get('info', {}).get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)

    if request.method == 'POST':
        team_names = request.POST.get('team_names')
        stadium_name = request.POST.get('stadium_name')
        start_datetime = request.POST.get('start_datetime')
        id_pertandingan = request.POST.get('id_pertandingan')

        redirect_url = reverse('example_app:rapat') + f'?team_names={team_names}&stadium_name={stadium_name}&start_datetime={start_datetime}&id_pertandingan={id_pertandingan}'
        return HttpResponseRedirect(redirect_url)
    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT T.id_pertandingan AS id_pertandingan, string_agg(T.nama_tim, ' vs ') AS team_names, S.nama AS stadium_name, P.start_datetime
            FROM PERTANDINGAN AS P
            JOIN STADIUM AS S ON P.stadium = S.id_stadium
            JOIN TIM_PERTANDINGAN AS T ON T.id_pertandingan = P.id_pertandingan
            GROUP BY S.nama, P.start_datetime, T.id_pertandingan;
        """)

        pertandingans = dict_fetch_all(cursor)
        for pertandingan in pertandingans:
            start_datetime = pertandingan['start_datetime']
            pertandingan['start_datetime_tampilan'] = start_datetime
            formatted_datetime = datetime.strftime(start_datetime, "%Y-%m-%d")
            pertandingan['start_datetime'] = formatted_datetime
 
        context['pertandingans'] = pertandingans

    return render(request, 'mulai_rapat.html', context)

def rapat(request):
    username = request.session.get('info', {}).get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)

    team_names = request.GET.get('team_names')
    stadium_name = request.GET.get('stadium_name')
    start_datetime = request.GET.get('start_datetime')
    id_pertandingan = request.GET.get('id_pertandingan')

    if request.method == 'POST':
        # Process the form submission
        team_names = request.POST.get('team_names')
        stadium_name = request.POST.get('stadium_name')
        start_datetime = request.POST.get('start_datetime')
        id_pertandingan = request.POST.get('id_pertandingan')
        isi_rapat = request.POST.get('isi_rapat')
        username = request.session['info'].get('username')
        perwakilan_panitia = get_user_id(username)
        team_names_split = team_names.split(" vs ")
        manajer_tim_a = get_manajer_id_by_team(team_names_split[0])
        manajer_tim_b = get_manajer_id_by_team(team_names_split[1])
        start_datetime_obj = datetime.strptime(start_datetime, "%Y-%m-%d")
        datetime_now = (start_datetime_obj - timedelta(days=3)).strftime("%Y-%m-%d")
        random_time = datetime.now().replace(hour=random.randint(0, 23)).strftime("%H:%M:%S")
        datetime_now += " " + random_time
        with connection.cursor() as cursor:
            cursor.execute(f"""
                INSERT INTO Rapat (ID_Pertandingan, Datetime, Perwakilan_Panitia, Manajer_Tim_A, Manajer_Tim_B, Isi_Rapat) VALUES 
                ('{id_pertandingan}', '{datetime_now}', '{perwakilan_panitia}', 
                '{manajer_tim_a}', '{manajer_tim_b}', 
                '{isi_rapat}');
                """)
            return redirect('example_app:dashboard')

    context = {
        'team_names': team_names,
        'stadium_name': stadium_name,
        'start_datetime': start_datetime,
        'id_pertandingan': id_pertandingan,
        'user': {'role': f'{role}'}
    }

    return render(request, 'rapat.html', context)

def get_manajer_id_by_team(team):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id_manajer
            FROM TIM_MANAJER
            WHERE nama_tim = %s;
        """, [team])
        result = cursor.fetchone()
        if result is not None:
            return result[0]

    
