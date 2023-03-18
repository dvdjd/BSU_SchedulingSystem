from django.urls import path
from . import views

urlpatterns = [
    path('course_offer', views.course_offer, name='course_offer'),
    path('course_offering', views.course_offering, name='course_offering'),
    path('course_schedule', views.course_schedule, name='course_schedule'),
    path('search_course', views.search_course, name='search_course'),
    path('save_course_offering', views.save_course_offering, name='save_course_offering'),
    path('populate_section', views.populate_section, name='populate_section'),
    path('search_course_schedule', views.search_course_schedule, name='search_course_schedule'),
    
]