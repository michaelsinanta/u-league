from django.urls import path
from example_app.views import *
from example_app.cru_pengguna_views import login_user, logout_user, show_register
from example_app.dashboard_views import dashboard
from example_app.cru_peminjaman_stadium_views import peminjaman_stadium
from example_app.cr_mulai_rapat_views import mulai_rapat, rapat

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('landing-page/', landing_page, name='landing-page'),
    path('dashboard', dashboard, name='dashboard'),
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
    path('register', show_register , name='show_register'),
    path('form1', regis1, name='form1'),
    path('form2', regis2, name='form2'),
    path('mulai-rapat', mulai_rapat, name='mulai_rapat'),
    path('rapat', rapat, name='rapat'),
    path('mulai-pertandingan', mulai_pertandingan, name='mulai-pertandingan'),
    path('peristiwa', peristiwa, name='peristiwa'),
    path('register-tim', register_tim, name='register_tim'),
    path('peminjaman-stadium', peminjaman_stadium, name='peminjaman_stadium'),
    path('my-team', my_team, name='my_team'),
]