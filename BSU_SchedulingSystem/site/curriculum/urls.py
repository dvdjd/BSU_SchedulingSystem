from django.urls import path
from . import views

urlpatterns = [
    path('curriculum', views.curriculum, name='curriculum'),
    path('generate_schedule', views.generate_schedule, name='generate_schedule'),
    path('search_schedule', views.search_schedule, name='search_schedule'),
    path('add_schedule', views.add_schedule, name='add_schedule'),
    path('add_subject', views.add_subject, name='add_subject'),
    path('populate_programcode', views.populate_programcode, name='populate_programcode'),
    path('populate_name', views.populate_name, name='populate_name'),
    path('save_curriculum', views.save_curriculum, name='save_curriculum'),
    path('save_schedule', views.save_schedule, name='save_schedule'),
    path('get_curriculum', views.get_curriculum, name='get_curriculum'),
    path('update_curriculum', views.update_curriculum, name='update_curriculum'),
    path('add_instructor_schedule', views.add_instructor_schedule, name='add_instructor_schedule'),
    path('get_schedule', views.get_schedule, name='get_schedule'),
    path('update_instructor_schedule', views.update_instructor_schedule, name='update_instructor_schedule'),
    path('delete_instructor_schedule', views.delete_instructor_schedule, name='delete_instructor_schedule'),
    path('add_student_schedule', views.add_student_schedule, name='add_student_schedule'),
    path('populate_irreg_student', views.populate_irreg_student, name='populate_irreg_student'),
    path('save_irreg_student', views.save_irreg_student, name='save_irreg_student'),
    path('delete_student_schedule', views.delete_student_schedule, name='delete_student_schedule'),
    path('populate_subject', views.populate_subject, name='populate_subject'),
    path('get_subjects', views.get_subjects, name='get_subjects'),
    path('delete_subject', views.delete_subject, name='delete_subject'),
    path('delete_schedule', views.delete_schedule, name='delete_schedule'),
]