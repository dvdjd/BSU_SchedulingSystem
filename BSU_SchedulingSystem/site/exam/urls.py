from django.urls import path
from . import views

urlpatterns = [
    path('exam', views.exam, name='exam'),
    path('add_exam_schedule', views.add_exam_schedule, name='add_exam_schedule'),
]