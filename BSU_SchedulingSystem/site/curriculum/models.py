from django.db import models

LEVEL = (
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
)

PERIOD = (
    ('1', '1st Semester'),
    ('2', '2nd Semester'),
    ('3', 'Midterm'),
)

# Create your models here.
class AcademicProgramModel(models.Model):
    program_code = models.CharField(max_length=20, unique=True)
    program_description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.program_code
    
class CourseModel(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    program_code = models.ForeignKey(AcademicProgramModel,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_code
    
class CurriculumYearModel(models.Model):
    curriculum_year = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.curriculum_year
    
class SectionModel(models.Model):
    section_code = models.CharField(max_length=20, unique=True)
    level = models.CharField(max_length=20,choices=LEVEL)
    
    def __str__(self):
        return self.section_code
    
    
class SubjectModel(models.Model):
    subject_code = models.CharField(max_length=20, unique=True)
    subject_description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_code
    
class CurriculumModel(models.Model):
    curriculum_year = models.ForeignKey(CurriculumYearModel,on_delete=models.CASCADE)
    period = models.CharField(max_length=20,choices=PERIOD)
    level = models.CharField(max_length=20,choices=LEVEL)
    subject_code = models.ForeignKey(SubjectModel,on_delete=models.CASCADE)
    course_code = models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    program_code = models.CharField(max_length=20)
    lecture = models.IntegerField()
    lab = models.IntegerField() 
    units = models.IntegerField()
    
class InstructorModel(models.Model):
    instructor_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    days = models.CharField(null=True, max_length=50)
    time_in = models.IntegerField(null=True)
    time_out = models.IntegerField(null=True)
    college = models.CharField(max_length=10)
    academic_year = models.CharField(max_length=10)
    section = models.CharField(max_length=20)
    semester = models.IntegerField()
    subject_code = models.CharField(max_length=50)
    units = models.IntegerField()
    room = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)

class SubjectScheduleModel(models.Model):
    profesor = models.CharField(max_length=50)
    days = models.CharField(null=True, max_length=50)
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    subject_code = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=10)
    section = models.CharField(max_length=20)
    semester = models.IntegerField()
    units = models.IntegerField()