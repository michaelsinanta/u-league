from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def peminjaman_stadium(request):
    username = request.session['info'].get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Manajer":
        return render(request, 'landing_page.html', context)

    id_manajer = get_user_id(username)

    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT S.nama, P.start_datetime, P.end_datetime
            FROM STADIUM AS S, PEMINJAMAN AS P
            WHERE P.id_manajer = '{id_manajer}' AND P.id_stadium = S.id_stadium;
        """)

        peminjamans = dict_fetch_all(cursor)
        for peminjaman in peminjamans:
            start_datetime = peminjaman['start_datetime']
            end_datetime = peminjaman['end_datetime']
            start_datetime = timezone.localtime(start_datetime)
            end_datetime = timezone.localtime(end_datetime)
            formatted_start_datetime = datetime.strftime(start_datetime, "%b. %d, %Y, %H:%M")
            formatted_end_datetime = datetime.strftime(end_datetime, "%b. %d, %Y, %H:%M")
            peminjaman['start_datetime_tampilan'] = formatted_start_datetime
            peminjaman['end_datetime_tampilan'] = formatted_end_datetime
            peminjaman['start_end_datetime_tampilan'] = f"{formatted_start_datetime} - {formatted_end_datetime}"
        context['peminjamans'] = peminjamans

        cursor.execute("""
            SELECT nama, id_stadium
            FROM STADIUM;
        """)
        stadiums = dict_fetch_all(cursor)
        context['stadiums'] = stadiums

    return render(request, 'peminjaman_stadium.html', context)

def list_waktu_peminjaman_stadium(request):
    username = request.session['info'].get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Manajer":
        return render(request, 'landing_page.html', context)
    
    id_manajer = get_user_id(username)

    stadium_name = request.GET.get('stadium_name')
    id_stadium = request.GET.get('id_stadium')
    date = request.GET.get('date')

    if request.method == 'POST':
        id_stadium = request.POST.get('id_stadium')
        start_hours = request.POST.get('start_hours')
        end_hours = request.POST.get('end_hours')
        date = request.POST.get('date')
        with connection.cursor() as cursor:
            try :
                cursor.execute(f"""
                    insert into Peminjaman (id_manajer, start_datetime, end_datetime, id_stadium) values                 
                    ('{id_manajer}', '{date + " " + start_hours}', '{date + " " + end_hours}', '{id_stadium}');
                    """)
            except Exception as e:
                return JsonResponse({
                    "message" : str(e).split('\n')[0],
                    "status" : 400
                })

            return JsonResponse({"message": "Peminjaman stadium sukses", "status": 200})

    context = {
        'stadium_name': stadium_name,
        'id_stadium' : id_stadium,
        'date' : date,
        'user': {'role': f'{role}'}
    }

    return render(request, 'list_waktu_peminjaman_stadium.html', context)
