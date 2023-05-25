import uuid
from django.db import connection
from example_app.utils import dict_fetch_all, get_user_role, get_user_id
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from example_app.r_list_pertandingan_views import get_nama_tim_bertanding
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.template.loader import render_to_string




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

@csrf_exempt
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
    
    tanggal = request.GET.get('tanggal', None)
    tanggal = datetime.strptime(tanggal, "%Y-%m-%d")
    
    cursor = connection.cursor()

    cursor.execute(f"""
                   SELECT * FROM pertandingan WHERE stadium = '{id_stadium}' AND start_datetime > '{tanggal}'
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
        "data": list_nama_tim_bertanding,
    }

    return render(request, 'pilih_pertandingan.html', context)

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
        try  :
            cursor.execute(f"""
                INSERT INTO pembelian_tiket 
                (nomor_receipt, id_penonton, jenis_tiket, jenis_pembayaran, id_pertandingan)
                VALUES ('{receipt}', '{id_penonton}', '{jenis_tiket}', '{jenis_pembayaran}', '{id_pertandingan}');
                """)
            
        except Exception as e :
            return JsonResponse({"response" : str(e)}, status=400)

        
        cursor.execute(f"""
                       SELECT * from pertandingan WHERE id_pertandingan = '{id_pertandingan}'
                       """)
        pertandingan = dict_fetch_all(cursor)[0]
        cursor.execute(f"""
                       SELECT * from stadium WHERE id_stadium = '{pertandingan['stadium']}'
                       """)
        
        stadium = dict_fetch_all(cursor)[0]
        kapasitas_stadium = stadium['kapasitas'] - 1
        
        cursor.execute(f"""
                       UPDATE stadium SET kapasitas = {kapasitas_stadium} WHERE id_stadium = '{stadium['id_stadium']}'
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
    
