from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pembuatan_pertandingan(request):
    return render(request, 'pembuatan_pertandingan.html')