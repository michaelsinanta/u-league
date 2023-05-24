from django.db import connection
from example_app.utils import dict_fetch_all, get_user_role
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from uuid import uuid4;


def get_nama_tim_bertanding(list_pertandingan, list_tim_pertandingan) :
    tim_bertanding = []

    for i in list_pertandingan : 
        counter = 0
        new_dict = {
            "id_pertandingan" : "",
            "id_stadium" : "",
            "nama_tim_bertanding" : "",
            "tanggal_mulai" : ""
        }
        for j in list_tim_pertandingan :
            if(i["id_pertandingan"] == j["id_pertandingan"]) :
                counter += 1
                new_dict['id_stadium'] = i['stadium']
                new_dict['id_pertandingan'] = i['id_pertandingan']
                if(counter == 1) : 
                    new_dict['nama_tim_bertanding'] = new_dict["nama_tim_bertanding"] + j['nama_tim'] + " vs "
                    continue
                
                new_dict['nama_tim_bertanding'] = new_dict["nama_tim_bertanding"] + j['nama_tim']                
                if(counter == 2) :
                    new_dict['tanggal_mulai'] = i['start_datetime']
                    tim_bertanding.append(new_dict)
                    break;
    return tim_bertanding

def get_stadium(tim_bertanding, list_stadium):
    for i in tim_bertanding :
        for j in list_stadium :
            if(i['id_stadium'] == j['id_stadium']) :
                i['nama_stadium'] = j['nama']
    return tim_bertanding

def get_list_pertandingan(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }
    print(role)
    if(role != "Manajer" and role != "Penonton") :
        return render(request, 'landing_page.html', context)
    
    cursor = connection.cursor()
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
    context = {
                'user': {
                    'role': f'{role}',
                },
               "data" : list_nama_tim_bertanding
               }
    return render(request, 'list_pertandingan.html', context)


   