from example_app.utils import get_user_role, dict_fetch_all
from django.shortcuts import redirect, render
from django.db import connection

def dashboard(request):
    username = request.COOKIES.get('username', None)

    if username is None:
        return render(request, 'landing_page.html', {}) 

    role = get_user_role(username)
    context = {
        'user': {
            'role': f'{role}',
        }
    }

    if role == "Manajer":
        with connection.cursor() as cursor:
            cursor.execute(f'''
                SELECT N.nama_depan, N.nama_belakang, N.nomor_hp, N.email, N.alamat, S.status
                FROM NON_PEMAIN AS N, MANAJER AS M, STATUS_NON_PEMAIN AS S
                WHERE M.username = '{username}' AND M.id_manajer = N.id AND N.id = S.ID_Non_Pemain;
            ''')
            user_list = dict_fetch_all(cursor)
            context = {
                'user_list': user_list,
                'user': {
                    'role': f'{role}',
                }
            }
            return render(request, 'dashboard_manajer.html', context)
    elif role == "Panitia":
        return render(request, 'dashboard_panitia.html', context)
    elif role == "Penonton":
        return render(request, 'dashboard_penonton.html', context)
    else :
        return render(request, 'landing_page.html')
    
    
