from django.urls import path
from . import views

urlpatterns = [
    path('exam', views.exam, name='exam'),
    path('add_exam_schedule', views.add_exam_schedule, name='add_exam_schedule'),
    path('delete_exam_schedule', views.delete_exam_schedule, name='delete_exam_schedule'),
    path('modify_exam_schedule', views.modify_exam_schedule, name='modify_exam_schedule'),
    path('save_exam_schedule', views.save_exam_schedule, name='save_exam_schedule'),
]