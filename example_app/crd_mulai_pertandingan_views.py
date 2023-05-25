from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render
from datetime import datetime

def mulai_pertandingan(request):
    username = request.COOKIES.get('username')


def get_list_pertandingan(request):
    context = {}
    with connection.cursor() as cursor:
            datetime_now = datetime.now().strftime("%Y-%m-%d")
            
            cursor.execute(f"""
                SELECT T.id_pertandingan AS id_pertandingan, string_agg(T.nama_tim, ' vs ') AS team_names, P.start_datetime
                FROM PERTANDINGAN AS P
                JOIN TIM_PERTANDINGAN AS T ON T.id_pertandingan = P.id_pertandingan
                WHERE P.START_DATETIME > '{datetime_now}'
                GROUP BY P.start_datetime, T.id_pertandingan;
            """)
            list_pertandingan = dict_fetch_all(cursor)
            
            context['list_pertandingan'] = list_pertandingan
            return render(request, 'dashboard_panitia.html', context)