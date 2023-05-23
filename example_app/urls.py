from django.urls import path
from example_app.views import *
from example_app.cru_pengguna_views import login_user, logout_user, show_register, form_manajer, form_penonton, form_panitia, register_manajer, register_panitia, register_penonton
from example_app.dashboard_views import dashboard
from example_app.cru_manajer_views import show_tim, remove_pemain

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
    path('register-manajer', form_manajer, name='form_manajer'),
    path('register-penonton', form_penonton, name='form_penonton'),
    path('register-panitia', form_panitia, name='form_panitia'),
    path('mulai-rapat', mulai_rapat, name='mulai-rapat'),
    path('rapat', rapat, name='rapat'),
    path('mulai-pertandingan', mulai_pertandingan, name='mulai-pertandingan'),
    path('peristiwa', peristiwa, name='peristiwa'),
    path('register-tim', register_tim, name='register_tim'),
    path('peminjaman', peminjaman_stadium, name='peminjaman_stadium'),
    path('my-team', show_tim, name='show_tim'),
    path('remove-pemain/<str:id>', remove_pemain, name='remove_pemain'),
    path('add-manajer', register_manajer, name='register_manajer'),
    path('add-penonton', register_penonton, name='register_penonton'),
    path('add-panitia', register_panitia, name='register_panitia')
]