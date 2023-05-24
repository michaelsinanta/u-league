from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection
from django.shortcuts import redirect, render
from example_app.utils import dict_fetch_all
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4;
from django.views.decorators.csrf import csrf_exempt

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        response = HttpResponse()
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            cursor.execute(f'''
                SELECT *
                FROM User_System
                WHERE username='{username}' AND password='{password}';
            ''')
            user_list = dict_fetch_all(cursor)
        if len(user_list) != 0:  # User found
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            response.status_code = 200
            return response
            
        else:  # User not found
            response.delete_cookie('username')
            response.delete_cookie('password')
            response.status_code = 404
            return response
    return HttpResponse(status=404)

def show_register(request):
    return render(request, 'pengguna.html', {})

def logout_user(request):
    response = HttpResponseRedirect('/landing-page')
    response.delete_cookie('username')
    response.delete_cookie('password')
    return response

def form_manajer(request):
    return render(request, 'form_regis_manajer.html')

def form_penonton(request):
    return render(request, 'form_regis_penonton.html')

def form_panitia(request):
    return render(request, 'form_regis_panitia.html')

@csrf_exempt
def register_manajer(request):
    if request.method == 'GET':
        return render(request, 'form_regis_manajer.html')
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'''
                    INSERT INTO USER_SYSTEM VALUES
                    ('{username}', '{password}');
                ''')
            except Exception as e:
                return JsonResponse({
                    "message":str(e).split("\n")[0],
                    "status":409
                })

            _id = uuid4()
            nama_depan = request.POST.get('fname')    
            nama_belakang = request.POST.get('lname')    
            nomor_hp = request.POST.get('nohp')    
            email = request.POST.get('email')    
            alamat = request.POST.get('alamat')
            status = request.POST.get('status')

            if nama_depan != " " or nama_belakang != " " or nomor_hp != " " or email != " " or alamat != " ":
                cursor.execute(f'''
                    INSERT INTO NON_PEMAIN VALUES
                    ('{_id}', '{nama_depan}', '{nama_belakang}', '{nomor_hp}', '{email}', '{alamat}');
                ''')

                cursor.execute(f'''
                    INSERT INTO STATUS_NON_PEMAIN VALUES
                    ('{_id}', '{status}');
                ''')

                cursor.execute(f'''
                    INSERT INTO MANAJER VALUES
                    ('{_id}', '{username}');
                ''')
                
                return JsonResponse({
                    "message":"Success!",
                    "status":200
                })
            else:
                return redirect('example_app:form_manajer')

        
@csrf_exempt
def register_penonton(request):
    if request.method == 'GET':
        return render(request, 'form_regis_penonton.html')
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'''
                    INSERT INTO USER_SYSTEM VALUES
                    ('{username}', '{password}');
                ''')
            except Exception as e:
                return JsonResponse({"message":str(e).split("\n")[0], "status":409})
                
            _id = uuid4()
            nama_depan = request.POST.get('fname')    
            nama_belakang = request.POST.get('lname')    
            nomor_hp = request.POST.get('nohp')    
            email = request.POST.get('email')    
            alamat = request.POST.get('alamat')
            status = request.POST.get('status')

            if nama_depan != " " or nama_belakang != " " or nomor_hp != " " or email != " " or alamat != " ":
                cursor.execute(f'''
                    INSERT INTO NON_PEMAIN VALUES
                    ('{_id}', '{nama_depan}', '{nama_belakang}', '{nomor_hp}', '{email}', '{alamat}');
                ''')

                cursor.execute(f'''
                    INSERT INTO STATUS_NON_PEMAIN VALUES
                    ('{_id}', '{status}');
                ''')

                cursor.execute(f'''
                    INSERT INTO PENONTON VALUES
                    ('{_id}', '{username}');
                ''')
                
                return JsonResponse({
                    "message":"Success!",
                    "status":200
                })
            else:
                return redirect('example_app:form_penonton')

            
@csrf_exempt
def register_panitia(request):
    if request.method == 'GET':
        return render(request, 'form_regis_panitia.html')
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'''
                    INSERT INTO USER_SYSTEM VALUES
                    ('{username}', '{password}');
                ''')

            
            except Exception as e:
                return JsonResponse({"message":str(e).split("\n")[0], "status":409})

            _id = uuid4()
            nama_depan = request.POST.get('fname')    
            nama_belakang = request.POST.get('lname')    
            nomor_hp = request.POST.get('nohp')    
            email = request.POST.get('email')    
            alamat = request.POST.get('alamat')
            status = request.POST.get('status')
            jabatan = request.POST.get('jabatan')

            if nama_depan != " " or nama_belakang != " " or nomor_hp != " " or email != " " or alamat != " " or jabatan != " ":
                cursor.execute(f'''
                    INSERT INTO NON_PEMAIN VALUES
                    ('{_id}', '{nama_depan}', '{nama_belakang}', '{nomor_hp}', '{email}', '{alamat}');
                ''')

                cursor.execute(f'''
                    INSERT INTO STATUS_NON_PEMAIN VALUES
                    ('{_id}', '{status}');
                ''')

                cursor.execute(f'''
                    INSERT INTO PANITIA VALUES
                    ('{_id}', '{jabatan}','{username}');
                ''')
                
                return JsonResponse({
                    "message":"Success!",
                    "status":200
                })
            else:
                return redirect('example_app:form_panitia')

            
                