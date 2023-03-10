from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change_password', views.change_password, name='change_password'),
    path('add_user', views.add_user, name='add_user'),
    path('logout', views.logout, name='logout'),
]