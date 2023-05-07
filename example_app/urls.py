from django.urls import path
from example_app.views import index, dashboardManajer, dashboardPenonton, dashboardPanitia, login, manage_pertanding, landing_page

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('landing-page/', landing_page, name='landing-page'),
    path('manage-pertandingan/', manage_pertanding, name='manage-pertandingan'),
    path('dashboard-manajer', dashboardManajer, name='dashboardManajer'),
    path('dashboard-penonton', dashboardPenonton, name='dashboardPenonton'),
    path('dashboard-panitia', dashboardPanitia, name='dashboardPanitia'),
]