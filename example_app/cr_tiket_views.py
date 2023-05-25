import uuid
from django.db import connection
from example_app.utils import dict_fetch_all, get_user_role, get_user_id
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from example_app.r_list_pertandingan_views import get_nama_tim_bertanding
from django.views.decorators.csrf import csrf_exempt


def pilih_stadium(request) :
    username = request.session.get('info', {}).get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }
    if(role != 'Penonton') :
        return render(request, 'landing_page.html', context)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stadium")
    list_stadium = dict_fetch_all(cursor)
    context = {
        'user': {
            'role': f'{role}',
        },
        "data" : list_stadium
    }
    return render(request, 'pilih_stadium.html', context)

def pilih_pertandingan(request, id_stadium) :
    username = request.session.get('info', {}).get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }
    if(role != 'Penonton') :
        return render(request, 'landing_page.html', context)
    
    cursor = connection.cursor()
    cursor.execute(f"""
                   SELECT * FROM pertandingan WHERE stadium = '{id_stadium}'
                   """)
    list_pertandingan = dict_fetch_all(cursor)
    
    cursor.execute("""
                   SELECT * FROM tim_pertandingan
                   """)
    
    list_tim_pertandingan = dict_fetch_all(cursor)
    
    list_nama_tim_bertanding = get_nama_tim_bertanding(list_pertandingan, list_tim_pertandingan)
    for i in list_nama_tim_bertanding :
        i['nama_tim_bertanding'] = i['nama_tim_bertanding'].split(' ')
        i['tim_1'] = i['nama_tim_bertanding'][0]
        i['tim_2'] = i['nama_tim_bertanding'][2]

        
    context = {
        'user': {
            'role': f'{role}',
        },
        "data": list_nama_tim_bertanding
    }
        
    return render(request, "pilih_pertandingan.html", context)

@csrf_exempt
def beli_tiket(request, id_pertandingan) :
    username = request.session.get('info', {}).get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 

    role = get_user_role(username)
    context = {
        'user': {
            'role': f'{role}',
        }
    }
    if(role != 'Penonton') :
        return render(request, 'landing_page.html', {}) 

    id_penonton = get_user_id(username)
    if(request.method == "POST") :
        receipt = uuid.uuid4()
        id_pertandingan = request.POST.get('id_pertandingan')
        jenis_tiket = request.POST.get("jenis_tiket")
        jenis_pembayaran = request.POST.get("jenis_pembayaran")
        
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO pembelian_tiket 
            (nomor_receipt, id_penonton, jenis_tiket, jenis_pembayaran, id_pertandingan)
            VALUES ('{receipt}', '{id_penonton}', '{jenis_tiket}', '{jenis_pembayaran}', '{id_pertandingan}');
            """)
        
        return HttpResponse(status=200)
    else :
        context = {
        'user': {
            'role': f'{role}',
        },
            "data" : id_pertandingan
        }
        return render(request, "beli_tiket.html", context)
    
