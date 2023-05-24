from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render

def peminjaman_stadium(request):
    username = request.COOKIES.get('username')

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
            SELECT S.nama, P.start_datetime
            FROM STADIUM AS S, PEMINJAMAN AS P
            WHERE P.id_manajer = '{id_manajer}' AND P.id_stadium = S.id_stadium;
        """)

        peminjamans = dict_fetch_all(cursor)
        context['peminjamans'] = peminjamans

        cursor.execute(f"""
            SELECT nama, id_stadium
            FROM STADIUM;
        """)
        stadiums = dict_fetch_all(cursor)
        context['stadiums'] = stadiums
    
    return render(request, 'peminjaman_stadium.html', context)