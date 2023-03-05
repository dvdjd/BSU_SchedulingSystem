from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change_password', views.change_password, name='change_password'),
    path('logout', views.logout, name='logout'),
]