from django.urls import path
from example_app.views import index

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', index, name='login'),
    path('manage-pertandingan/', index, name='manage-pertandingan'),
]