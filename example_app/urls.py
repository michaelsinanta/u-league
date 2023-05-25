from django.urls import path
from example_app.views import *
from example_app.cru_pengguna_views import login_user, logout_user, show_register, form_manajer, form_penonton, form_panitia, register_manajer, register_panitia, register_penonton
from example_app.dashboard_views import dashboard
from example_app.r_list_pertandingan_views import get_list_pertandingan
from example_app.cr_tiket_views import pilih_stadium, pilih_pertandingan, beli_tiket
from example_app.r_history_rapat_views import history_rapat, lihat_laporan_rapat
from example_app.cru_peminjaman_stadium_views import peminjaman_stadium, list_waktu_peminjaman_stadium
from example_app.cr_mulai_rapat_views import mulai_rapat, rapat
from example_app.cru_manajer_views import show_tim, remove_pemain, add_tim, add_pemain, make_captain, add_pelatih, remove_pelatih
from example_app.crud_pembuatan_pertandingan_views import show_pembuatan_pertandingan, show_list_waktu_stadium, buat_pertandingan, add_pertandingan

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
    path('beli-tiket/<str:id_pertandingan>', beli_tiket, name='beli_tiket'),
    path('pilih-pertandingan/<str:id_stadium>', pilih_pertandingan, name='pilih_pertandingan'),
    path('pilih-stadium', pilih_stadium, name='pilih_stadium'),
    path('manage-pertandingan/', manage_pertanding, name='manage-pertandingan'),
    path('pembuatan-pertandingan', show_pembuatan_pertandingan, name='pembuatan_pertandingan'),
    path('list-waktu-stadium', show_list_waktu_stadium, name='list_waktu_stadium'),
    path('buat-pertandingan', buat_pertandingan, name='buat_pertandingan_antar_2tim'),
    path('list-pertandingan', get_list_pertandingan, name='list_pertandingan'),
    path('history-rapat', history_rapat, name='history_rapat'),
    path('lihat-laporan-rapat/<str:id_pertandingan>', lihat_laporan_rapat, name='lihat_laporan_rapat'),
    path('register', show_register , name='show_register'),
    path('mulai-rapat', mulai_rapat, name='mulai_rapat'),
    path('register-manajer', form_manajer, name='form_manajer'),
    path('register-penonton', form_penonton, name='form_penonton'),
    path('register-panitia', form_panitia, name='form_panitia'),
    path('rapat', rapat, name='rapat'),
    path('mulai-pertandingan', mulai_pertandingan, name='mulai-pertandingan'),
    path('peristiwa', peristiwa, name='peristiwa'),
    path('register-tim', register_tim, name='register_tim'),
    path('peminjaman-stadium', peminjaman_stadium, name='peminjaman_stadium'),
    path('list-waktu-peminjaman-stadium', list_waktu_peminjaman_stadium, name='list_waktu_peminjaman_stadium'),
    path('my-team', show_tim, name='show_tim'),
    path('remove-pemain/<str:id_pemain>', remove_pemain, name='remove_pemain'),
    path('add-manajer', register_manajer, name='register_manajer'),
    path('add-penonton', register_penonton, name='register_penonton'),
    path('add-panitia', register_panitia, name='register_panitia'),
    path('add-tim', add_tim, name='add_tim'),
    path('add-pemain', add_pemain, name='add_pemain'),
    path('make-captain/<str:id_pemain>', make_captain, name='make_captain'),
    path('add-pelatih', add_pelatih, name='add_pelatih'),
    path('remove-pelatih/<str:id_pelatih>', remove_pelatih, name='remove_pelatih'),
    path('add_pertandingan', add_pertandingan, name='add_pertandingan')
]