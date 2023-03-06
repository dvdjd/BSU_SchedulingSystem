from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('change_password', views.change_password, name='change_password'),
    path('add_instructor', views.add_instructor, name='add_instructor'),
    path('add_student', views.add_student, name='add_student'),
    path('logout', views.logout, name='logout'),
]