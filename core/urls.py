from django.urls import path

from . import views
from .views import *

urlpatterns =[
    path('list/', rps_list, name='rps_list'),
    path('play_user/<int:pk>', play_user, name='play-user'),
    path('play_user/compete/<int:pk>', rps_compete, name='rps_compete'),
    path('play_user/<int:pk>/rps_detail', rps_detail, name='rps_detail'),
    path('play_cpu/<int:pk>', play_cpu, name='play_cpu'),
]