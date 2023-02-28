from django.contrib import admin
from .models import StudentModel
from .forms import StudentAdminForm

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'instructor_id', 'level', 'course_code', 'subject_code')
    ordering = ('student_id', 'instructor_id', 'level', 'course_code', 'subject_code')
    search_fields = ('student_id',)
    form = StudentAdminForm
    
admin.site.register(StudentModel, StudentAdmin)