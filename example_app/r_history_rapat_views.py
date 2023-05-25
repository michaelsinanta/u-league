from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime

from example_app.r_list_pertandingan_views import get_nama_tim_bertanding, get_stadium

def history_rapat(request):
    username = request.session.get('info', {}).get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }
    
    if(role != "Manajer") :
        return render(request, 'landing_page.html', context)
    
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT * FROM rapat
                   """)
    list_rapat = dict_fetch_all(cursor)
    
    cursor.execute("""
                   SELECT * FROM pertandingan
                   """)
    list_pertandingan = dict_fetch_all(cursor)
    
    cursor.execute("""
                   SELECT * FROM tim_pertandingan
                   """)
    
    list_tim_pertandingan = dict_fetch_all(cursor)
    
    cursor.execute("""
                    Select * from stadium
                   """)
    
    list_stadium = dict_fetch_all(cursor)
    
    list_nama_tim_bertanding = get_nama_tim_bertanding(list_pertandingan, list_tim_pertandingan)
    list_nama_tim_bertanding = get_stadium(list_nama_tim_bertanding, list_stadium)
    
    res = []
    
    for i  in list_rapat :
        for j in list_nama_tim_bertanding :
            if(i['id_pertandingan'] == j['id_pertandingan']) :
                j['tanggal_mulai'] = i['datetime']
                j['perwakilan_panitia'] = i['perwakilan_panitia']
                res.append(j)
                break
            
    for i in res :
        cursor.execute(f"""
                Select username from panitia WHERE id_panitia = '{i['perwakilan_panitia']}'
                """)
        perwakilan_panitia = cursor.fetchone()[0]
        i['perwakilan_panitia'] = perwakilan_panitia
        
    
    context = {
        'user': {
            'role': f'{role}',
        },
        "data" : res
    }
    
    return render(request, 'history_rapat.html', context)

def lihat_laporan_rapat(request, id_pertandingan) :
    username = request.session.get('info', {}).get('username', None)
    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }
    
    if(role != "Manajer") :
        return render(request, 'landing_page.html', context)
    
    cursor = connection.cursor()
    cursor.execute(f"""
                   SELECT isi_rapat FROM rapat WHERE id_pertandingan = '{id_pertandingan}'
                   """)
    isi_rapat = cursor.fetchone()[0]
    context = {
        'user': {
            'role': f'{role}',
        },
        "data" : isi_rapat
    }
    
    return render(request, "lihat_laporan_rapat.html", context)