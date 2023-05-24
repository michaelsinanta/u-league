from django.urls import path
from example_app.views import index, dashboardManajer, dashboardPenonton, dashboardPanitia, login, manage_pertanding, landing_page
from example_app.r_list_pertandingan_views import *

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('landing-page/', landing_page, name='landing-page'),
    path('manage-pertandingan/', manage_pertanding, name='manage-pertandingan'),
    path('dashboard-manajer', dashboardManajer, name='dashboardManajer'),
    path('dashboard-penonton', dashboardPenonton, name='dashboardPenonton'),
    path('dashboard-panitia', dashboardPanitia, name='dashboardPanitia'),
    path('pembuatan-pertandingan', pembuatan_pertandingan, name='pembuatan_pertandingan'),
    path('list-waktu-stadium', list_waktu_stadium, name='list_waktu_stadium'),
    path('buat-pertandingan', buat_pertandingan_antar_2tim, name='buat_pertandingan_antar_2tim'),
    path('list-pertandingan', get_list_pertandingan, name='list_pertandingan'),
    path('history-rapat', history_rapat, name='history_rapat'),
]