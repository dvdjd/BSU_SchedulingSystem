from django.urls import path
from . import views

urlpatterns = [
    path('curriculum', views.curriculum, name='curriculum'),
    path('populate_programcode', views.populate_programcode, name='populate_programcode'),
]