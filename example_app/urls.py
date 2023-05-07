from django.urls import path
from example_app.views import index, register, peminjaman

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('peminjaman', peminjaman, name='peminjaman')
]