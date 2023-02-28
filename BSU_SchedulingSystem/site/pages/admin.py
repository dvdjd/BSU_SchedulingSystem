from django.contrib import admin
from .models import FacultyModel
from .forms import FacultyAdminForm

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('instructor_id', 'subject_code', 'room', 'days', 'time_in', 'time_out')
    ordering = ('instructor_id', 'subject_code', 'room', 'days', 'time_in', 'time_out')
    search_fields = ('instructor_id',)
    form = FacultyAdminForm
    
admin.site.register(FacultyModel, FacultyAdmin)
