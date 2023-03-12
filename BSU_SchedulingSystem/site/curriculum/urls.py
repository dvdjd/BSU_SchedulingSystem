from django.urls import path
from . import views

urlpatterns = [
    path('curriculum', views.curriculum, name='curriculum'),
    path('add_schedule', views.add_schedule, name='add_schedule'),
    path('populate_programcode', views.populate_programcode, name='populate_programcode'),
    path('save_curriculum', views.save_curriculum, name='save_curriculum'),
    path('get_curriculum', views.get_curriculum, name='get_curriculum'),
    path('update_curriculum', views.update_curriculum, name='update_curriculum'),
]