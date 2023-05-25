from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection
from django.shortcuts import redirect, render
from example_app.utils import dict_fetch_all, get_user_role
from django.views.decorators.csrf import csrf_exempt

LANDING_PAGE = 'example_app:show_tim'

def show_tim(request):
    username = request.session['info'].get('username')

    role = get_user_role(username)
    
    with connection.cursor() as cursor:
        username = request.session['info'].get('username')
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
            return redirect('example_app:register_tim')
        else:
            cursor.execute(f'''
                SELECT *
                FROM PEMAIN P
                JOIN TIM T ON T.NAMA_TIM=P.NAMA_TIM
                WHERE T.NAMA_TIM='{tim[0].get('nama_tim')}'
                ORDER BY NAMA_DEPAN;
            ''')
            list_pemain = dict_fetch_all(cursor)

            cursor.execute(f'''
                SELECT NP.ID, NP.NAMA_DEPAN, NP.NAMA_BELAKANG, NP.NOMOR_HP, NP.EMAIL, NP.ALAMAT, SP.SPESIALISASI
                FROM NON_PEMAIN NP
                JOIN PELATIH P ON NP.ID=P.ID_PELATIH
                JOIN SPESIALISASI_PELATIH SP ON SP.ID_PELATIH=P.ID_PELATIH
                JOIN TIM T ON T.NAMA_TIM=P.NAMA_TIM
                WHERE T.NAMA_TIM='{tim[0].get('nama_tim')}';
            ''')
            list_pelatih = dict_fetch_all(cursor)


            cursor.execute("""
                SELECT (NAMA_DEPAN || ' ' || NAMA_BELAKANG) AS NAMA, POSISI
                FROM PEMAIN
                WHERE NAMA_TIM IS NULL;
            """)

            list_available_pemain = dict_fetch_all(cursor)

            cursor.execute("""
                SELECT (NP.NAMA_DEPAN || ' ' || NP.NAMA_BELAKANG) AS NAMA, SP.SPESIALISASI
                FROM NON_PEMAIN NP
                JOIN PELATIH P ON P.ID_PELATIH=NP.ID
                JOIN SPESIALISASI_PELATIH SP ON SP.ID_PELATIH=P.ID_PELATIH
                WHERE P.NAMA_TIM IS NULL;
            """)

            list_available_pelatih = dict_fetch_all(cursor)
            
            context = {
                'user': {
                    'role':f'{role}'
                },
                'nama_tim':tim[0].get('nama_tim'),
                'list_pemain':list_pemain,
                'list_pelatih':list_pelatih,
                'list_available_pemain':list_available_pemain,
                'list_available_pelatih':list_available_pelatih
            }
            return render(request, 'my_team.html', context)

def remove_pemain(request, id_pemain):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            UPDATE PEMAIN
            SET NAMA_TIM=NULL
            WHERE ID_PEMAIN='{id_pemain}';
        ''')

        return redirect(LANDING_PAGE)
    
@csrf_exempt
def add_tim(request):
    if request.method == 'POST':
        username = request.session['info'].get('username')
        with connection.cursor() as cursor:

            cursor.execute(f'''
                SELECT ID_MANAJER
                FROM MANAJER
                WHERE USERNAME='{username}';
            ''')
            id_manajer = dict_fetch_all(cursor)[0].get('id_manajer')

            nama_tim = request.POST.get('namaTim')
            universitas = request.POST.get('universitas')

            try:
                cursor.execute(f'''
                    INSERT INTO TIM VALUES
                    ('{nama_tim}', '{universitas}');
                ''')
            except Exception:
                return JsonResponse({
                    "message":f'{nama_tim} already exists!',
                    "status": 409
                })

            cursor.execute(f'''
                INSERT INTO TIM_MANAJER VALUES
                ('{id_manajer}', '{nama_tim}');
            ''')

            return JsonResponse({
                "message":"Success!",
                "status":200
            })
    else:
        return redirect(LANDING_PAGE)

@csrf_exempt
def add_pemain(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            username = request.session['info'].get('username')

            cursor.execute(f'''
                SELECT TM.NAMA_TIM
                FROM TIM_MANAJER TM
                JOIN MANAJER M ON M.ID_MANAJER=TM.ID_MANAJER
                WHERE M.USERNAME='{username}';
            ''')

            nama_tim = dict_fetch_all(cursor)[0].get('nama_tim')
    
            nama_depan = request.POST.get('namaDepan')
            nama_belakang = request.POST.get('namaBelakang')

            cursor.execute(f'''
                UPDATE PEMAIN
                SET NAMA_TIM='{nama_tim}'
                WHERE NAMA_DEPAN='{nama_depan}' AND NAMA_BELAKANG='{nama_belakang}';
            ''')

            return JsonResponse({
                "message":"Berhasil menambahkan pemain",
                "status":200
            })
    else:
        return redirect(LANDING_PAGE)
    
def make_captain(request, id_pemain):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            UPDATE PEMAIN
            SET IS_CAPTAIN=TRUE
            WHERE ID_PEMAIN='{id_pemain}'
        ''')

        return redirect(LANDING_PAGE)

@csrf_exempt
def add_pelatih(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            username = request.session['info'].get('username')

            cursor.execute(f'''
                SELECT TM.NAMA_TIM
                FROM TIM_MANAJER TM
                JOIN MANAJER M ON M.ID_MANAJER=TM.ID_MANAJER
                WHERE M.USERNAME='{username}';
            ''')

            nama_tim = dict_fetch_all(cursor)[0].get('nama_tim')

            nama_depan = request.POST.get('namaDepan')
            nama_belakang = request.POST.get('namaBelakang')

            cursor.execute(f'''
                SELECT ID
                FROM NON_PEMAIN
                WHERE NAMA_DEPAN='{nama_depan}' AND NAMA_BELAKANG='{nama_belakang}';
            ''')
            
            id_pelatih = dict_fetch_all(cursor)[0].get('id')

            try:
                cursor.execute(f'''
                    UPDATE PELATIH
                    SET NAMA_TIM='{nama_tim}'
                    WHERE ID_PELATIH='{id_pelatih}';
                ''')

                return JsonResponse({
                    "message":"Berhasil menambahkan pelatih",
                    "status":200
                })
            
            except Exception as e:
                return JsonResponse({
                    'message':str(e).split('\n')[0],
                    'status':400
                })
    else:
        return redirect(LANDING_PAGE)


def remove_pelatih(request, id_pelatih):
    with connection.cursor() as cursor:
        cursor.execute(f'''
            UPDATE PELATIH
            SET NAMA_TIM=NULL
            WHERE ID_PELATIH='{id_pelatih}';
        ''')

        return redirect(LANDING_PAGE)


        