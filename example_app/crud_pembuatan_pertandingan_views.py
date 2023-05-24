from django.db import connection
from example_app.utils import get_user_role, dict_fetch_all, get_user_id
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

def show_buat_pertandingan(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)
    
    
def update_pertandingan(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)
    

def delete_pertandingan(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)

def add_pertandingan(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)

def show_list_waktu_stadium(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)

    stadium_name = request.GET.get('stadium_name')
    id_stadium = request.GET.get('id_stadium')
    date = request.GET.get('date')

def buat_pertandingan(request):
    username = request.COOKIES.get('username')

    if username is None:
        return render(request, 'landing_page.html', {}) 
    
    role = get_user_role(username)
    context = {
        'user': {'role': f'{role}'}
    }

    if role != "Panitia":
        return render(request, 'landing_page.html', context)