from django.urls import path
from . import views

urlpatterns = [
    path('course_offer', views.course_offer, name='course_offer'),
    path('course_schedule', views.course_schedule, name='course_schedule'),
    
]