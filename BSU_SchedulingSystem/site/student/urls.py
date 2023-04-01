from django.urls import path
from . import views

urlpatterns = [
    path('student', views.student, name='student'),
    path('student_calendar_details', views.student_calendar_details, name='student_calendar_details'),
]