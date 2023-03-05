from django.contrib import admin
from .models import ExamModel
from .forms import ExamAdminForm

class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'room', 'days', 'time_in', 'time_out')
    ordering = ('subject_code', 'room', 'days', 'time_in', 'time_out')
    search_fields = ('subject_code',)
    form = ExamAdminForm
    
admin.site.register(ExamModel, ExamAdmin)
