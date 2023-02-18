from django.urls import path
from . import views

urlpatterns = [
    path('exam', views.exam, name='exam'),
    
]