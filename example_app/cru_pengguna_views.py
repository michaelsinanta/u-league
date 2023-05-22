from django.http import HttpResponse
from django.db import connection
from django.shortcuts import redirect, render

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
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

def dict_fetch_all(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]