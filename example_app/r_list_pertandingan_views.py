from django.db import connection
from example_app.utils import dict_fetch_all
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def get_list_pertandingan(request):
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT * FROM pertandingan
                   """)
    list_pertandingan = dict_fetch_all(cursor)
    
    cursor.execute("""
                   SELECT * FROM tim_pertandingan
                   """)
    
    list_tim_pertandingan = dict_fetch_all(cursor)
    
    cursor.execute("""
                    Select * from stadium
                   """)
    
    list_stadium = dict_fetch_all(cursor)
    
    print(list_pertandingan)