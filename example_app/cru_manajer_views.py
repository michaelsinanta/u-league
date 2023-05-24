from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.shortcuts import redirect, render
from example_app.utils import dict_fetch_all

def show_tim(request):
    with connection.cursor() as cursor:
        username = request.COOKIES['username']
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
        
        if (len(tim) == 0):
            return render(request, 'register_tim.html')
        else:
            cursor.execute(f'''
                SELECT *
                FROM PEMAIN P
                JOIN TIM T ON T.NAMA_TIM=P.NAMA_TIM
                WHERE T.NAMA_TIM='{tim[0].get('nama_tim')}';
            ''')
            list_pemain = dict_fetch_all(cursor)

            cursor.execute(f'''
                SELECT NP.NAMA_DEPAN, NP.NAMA_BELAKANG, NP.NOMOR_HP, NP.EMAIL, NP.ALAMAT, SP.SPESIALISASI
                FROM NON_PEMAIN NP
                JOIN PELATIH P ON NP.ID=P.ID_PELATIH
                JOIN SPESIALISASI_PELATIH SP ON SP.ID_PELATIH=P.ID_PELATIH
                JOIN TIM T ON T.NAMA_TIM=P.NAMA_TIM
                WHERE T.NAMA_TIM='{tim[0].get('nama_tim')}';
            ''')
            list_pelatih = dict_fetch_all(cursor)

            context = {
                'nama_tim':tim[0].get('nama_tim'),
                'list_pemain':list_pemain,
                'list_pelatih':list_pelatih
            }
            return render(request, 'my_team.html', context)

def remove_pemain(request, id_pemain):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            UPDATE PEMAIN
            SET NAMA_TIM='{None}'
            WHERE ID_PEMAIN='{id_pemain}';
        ''')

        return redirect('example_app:show_tim')
    
def add_tim(request):
    if request.method == 'POST':
        username = request.COOKIES['username']
        with connection.cursor() as cursor:

            cursor.execute(f'''
                SELECT ID_MANAJER
                FROM MANAJER
                WHERE USERNAME='{username}';
            ''')
            id_manajer = dict_fetch_all(cursor)[0].get('id_manajaer')

            nama_tim = request.POST.get('nama_tim')
            universitas = request.POST.get('universitas')

            cursor.execute(f'''
                INSERT INTO TIM VALUES
                ('{nama_tim}', '{universitas}');
            ''')

            cursor.execute(f'''
                INSERT INTO TIM_MANAJER VALUES
                ('{id_manajer}', '{nama_tim}');
            ''')



        