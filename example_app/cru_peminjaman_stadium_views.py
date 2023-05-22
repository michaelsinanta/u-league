from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all
from django.shortcuts import redirect, render

def peminjaman_stadium(request):
    username = request.COOKIES.get('username')

    context = {
        'user': {'role': f'{get_user_role(username)}'}
    }

    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT id_stadium, nama
            FROM STADIUM;
        """)

        stadiums = dict_fetch_all(cursor)
        context['stadiums'] = stadiums 
    
    return render(request, 'peminjaman_stadium.html', context)