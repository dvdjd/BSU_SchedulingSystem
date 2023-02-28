from django.contrib import admin
from .models import AcademicProgramModel, CourseModel, CurriculumYearModel, CurriculumModel, SubjectModel, SectionModel
from .forms import CurriculumAdminForm

class AcademicProgramModelAdmin(admin.ModelAdmin):
    list_display = ('program_code','program_description')

class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'program_code', 'course_name')
    
class CurriculumModelAdmin(admin.ModelAdmin):
    list_display = ('curriculum_year', 'period', 'level', 'program_code', 'course_code', 'lecture', 'lab', 'units')
    
    form = CurriculumAdminForm
    
    class Media:
        js = ('js/course_program_populate.js',)
        
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_description', 'course_code', 'program_code')
    
    form = CurriculumAdminForm
    
    class Media:
        js = ('js/course_program_populate.js',)
    
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ('section_code','level')

# Register your models here.
admin.site.register(AcademicProgramModel, AcademicProgramModelAdmin)
admin.site.register(CourseModel, CourseModelAdmin)
admin.site.register(CurriculumYearModel)
admin.site.register(CurriculumModel, CurriculumModelAdmin)
admin.site.register(SubjectModel, SubjectModelAdmin)
admin.site.register(SectionModel, SectionModelAdmin)