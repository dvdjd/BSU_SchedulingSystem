from django.urls import path
from . import views

urlpatterns = [
    path('curriculum', views.curriculum, name='curriculum'),
]