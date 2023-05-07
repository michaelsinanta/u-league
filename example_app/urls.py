from django.urls import path
from example_app.views import index, dashboardManajer, dashboardPenonton, dashboardPanitia

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard-manajer', dashboardManajer, name='dashboardManajer'),
    path('dashboard-penonton', dashboardPenonton, name='dashboardPenonton'),
    path('dashboard-panitia', dashboardPanitia, name='dashboardPanitia'),
]