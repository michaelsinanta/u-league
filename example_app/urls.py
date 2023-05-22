from django.urls import path
from example_app.views import *

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard-manajer', dashboard_manajer, name='dashboard_manajer'),
    path('dashboard-penonton', dashboard_penonton, name='dashboard_penonton'),
    path('dashboard-panitia', dashboard_panitia, name='dashboard_panitia'),
    path('beli-tiket', beli_tiket, name='beli_tiket'),
    path('list-waktu-stadium', list_waktu_stadium, name='list_waktu_stadium'),
    path('pilih-pertandingan', pilih_pertandingan, name='pilih_pertandingan'),
]