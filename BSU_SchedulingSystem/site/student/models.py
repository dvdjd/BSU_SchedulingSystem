from django.db import models

LEVEL = (
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
)

STATUS = (
    ('regular', 'Regular'), 
    ('irregular', 'Irregular'),
)

# Create your models here.
class StudentModel(models.Model):
    
    student_id = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL, default='Select Level')
    course_code = models.CharField(max_length=20)
    program_code = models.CharField(max_length=20)
    section_code = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS, default='Select Status')

    def __str__(self):
        return self.student_id

#For Irregular Students
class StudentScheduleModel(models.Model):
    student_id = models.CharField(max_length=20)
    faculty_schedule_id = models.CharField(max_length=20)
        