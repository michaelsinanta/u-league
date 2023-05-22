from django.urls import path
from example_app.views import index, dashboardManajer, dashboardPenonton, dashboardPanitia, login, manage_pertanding, landing_page
from example_app.views import *

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('landing-page/', landing_page, name='landing-page'),
    path('dashboard-manajer', dashboard_manajer, name='dashboard_manajer'),
    path('dashboard-penonton', dashboard_penonton, name='dashboard_penonton'),
    path('dashboard-panitia', dashboard_panitia, name='dashboard_panitia'),
    path('beli-tiket', beli_tiket, name='beli_tiket'),
    path('pilih-pertandingan', pilih_pertandingan, name='pilih_pertandingan'),
    path('manage-pertandingan/', manage_pertanding, name='manage-pertandingan'),
    path('pembuatan-pertandingan', pembuatan_pertandingan, name='pembuatan_pertandingan'),
    path('list-waktu-stadium', list_waktu_stadium, name='list_waktu_stadium'),
    path('buat-pertandingan', buat_pertandingan_antar_2tim, name='buat_pertandingan_antar_2tim'),
    path('list-pertandingan', list_pertandingan, name='list_pertandingan'),
    path('history-rapat', history_rapat, name='history_rapat'),
    path('pengguna', pengguna, name='pengguna'),
    path('form1', regis1, name='form1'),
    path('form2', regis2, name='form2'),
    path('mulai-rapat', mulai_rapat, name='mulai-rapat'),
    path('rapat', rapat, name='rapat'),
    path('mulai-pertandingan', mulai_pertandingan, name='mulai-pertandingan'),
    path('peristiwa', peristiwa, name='peristiwa'),
    path('register', register_tim, name='register_tim'),
    path('peminjaman', peminjaman_stadium, name='peminjaman_stadium'),
    path('my-team', my_team, name='my_team'),
]