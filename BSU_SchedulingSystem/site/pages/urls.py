from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('faculty', views.faculty, name='faculty'),
    # path('faculty_calendar_details', views.faculty_calendar_details, name='faculty_calendar_details'),
]