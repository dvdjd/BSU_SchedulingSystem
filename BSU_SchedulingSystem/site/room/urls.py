from django.urls import path
from . import views

urlpatterns = [
    path('room', views.room, name='room'),
    path('search_room', views.search_room, name='search_room'),
]