from example_app.utils import get_user_role, dict_fetch_all
from django.shortcuts import redirect, render
from django.db import connection
from datetime import datetime

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


            cursor.execute(f'''
            SELECT ID_MANAJER
            FROM MANAJER
            WHERE USERNAME='{username}';
            ''')
            id_manajer = dict_fetch_all(cursor)

            cursor.execute(f'''
            SELECT *
            FROM TIM_MANAJER
            WHERE ID_MANAJER='{id_manajer[0].get('id_manajer')}';
            ''')
            tim = dict_fetch_all(cursor)

            cursor.execute(f'''
                SELECT *
                FROM PEMAIN P
                JOIN TIM T ON T.NAMA_TIM=P.NAMA_TIM
                WHERE T.NAMA_TIM='{tim[0].get('nama_tim')}'
                ORDER BY NAMA_DEPAN;
            ''')
            list_pemain = dict_fetch_all(cursor)

            context['user_list'] = user_list
            context['is_tim'] = len(tim) > 0
            context['nama_tim'] = tim[0].get('nama_tim')
            context['list_pemain'] = list_pemain

            return render(request, 'dashboard_manajer.html', context)
    elif role == "Panitia":
        with connection.cursor() as cursor:
            cursor.execute(f'''
                SELECT N.nama_depan, N.nama_belakang, N.nomor_hp, N.email, N.alamat, S.status, P.jabatan
                FROM NON_PEMAIN AS N, PANITIA AS P, STATUS_NON_PEMAIN AS S
                WHERE P.username = '{username}' AND P.id_panitia = N.id AND N.id = S.ID_Non_Pemain;
            ''')
            user_list = dict_fetch_all(cursor)

            datetime_now = datetime.now().strftime("%Y-%m-%d")
            
            cursor.execute(f"""
                SELECT T.id_pertandingan AS id_pertandingan, string_agg(T.nama_tim, ' vs ') AS team_names, P.start_datetime
                FROM PERTANDINGAN AS P
                JOIN TIM_PERTANDINGAN AS T ON T.id_pertandingan = P.id_pertandingan
                WHERE P.START_DATETIME > '{datetime_now}'
                GROUP BY P.start_datetime, T.id_pertandingan;
            """)
            pertandingans = dict_fetch_all(cursor)
            
            context['user_list'] = user_list
            context['daftar_rapat'] = pertandingans
            context['available_rapat'] = len(pertandingans) > 0
            return render(request, 'dashboard_panitia.html', context)
    elif role == "Penonton":
        with connection.cursor() as cursor:
            cursor.execute(f'''
                SELECT N.nama_depan, N.nama_belakang, N.nomor_hp, N.email, N.alamat
                FROM NON_PEMAIN AS N, PENONTON AS P
                WHERE P.username = '{username}' AND P.id_penonton = N.id;
            ''')
            user_list = dict_fetch_all(cursor)

            datetime_now = datetime.now().strftime("%Y-%m-%d")
            id_penonton = get_id_penonton(username)

            cursor.execute(f"""
                SELECT PT.ID_PERTANDINGAN, PR.START_DATETIME
                FROM PEMBELIAN_TIKET PT
                JOIN PENONTON P ON P.ID_PENONTON=PT.ID_PENONTON
                JOIN PERTANDINGAN PR ON PR.ID_PERTANDINGAN=PT.ID_PERTANDINGAN
                WHERE PR.START_DATETIME > '{datetime_now}' AND PT.ID_PENONTON='{id_penonton}';
            """)

            pertandingans = dict_fetch_all(cursor)
            
            for pertandingan in pertandingans:
                pertandingan['nama_tim'] = get_nama_tim_pertandingan(pertandingan['id_pertandingan'])

            context['pertandingan'] = pertandingans
            context['user_list'] = user_list
            context['is_available'] = len(pertandingans) > 0
            return render(request, 'dashboard_penonton.html', context)
    else :
        return render(request, 'landing_page.html')
    
def get_nama_tim_pertandingan(id_pertandingan):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            SELECT STRING_AGG(T.NAMA_TIM, ' vs ') AS NAMA_TIM
            FROM TIM_PERTANDINGAN T
            WHERE ID_PERTANDINGAN='{id_pertandingan}'
        ''')
        result = cursor.fetchone();
        return result[0]
    
def get_id_penonton(username):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            SELECT ID_PENONTON
            FROM PENONTON
            WHERE USERNAME='{username}';
        ''')
        result = cursor.fetchone();
        return result[0]