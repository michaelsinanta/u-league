from django.urls import path
from example_app.views import *

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('pembuatan-pertandingan', pembuatan_pertandingan, name='pembuatan_pertandingan'),
    path('list-waktu-stadium', list_waktu_stadium, name='list_waktu_stadium'),
    path('buat-pertandingan', buat_pertandingan_antar_2tim, name='buat_pertandingan_antar_2tim'),
    path('list-pertandingan', list_pertandingan, name='list_pertandingan'),
    path('history-rapat', history_rapat, name='history_rapat'),
]