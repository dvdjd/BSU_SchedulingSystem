from django.db import models
from room.models import RoomModel
from curriculum.models import SubjectModel

LEVEL = (
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
)

# Create your models here.
class FacultyModel(models.Model):

    instructor_id = models.CharField(max_length=20)
    subject_code = models.CharField(max_length=20)
    room = models.CharField(max_length=20)
    section_code = models.CharField(max_length=20)
    course_code = models.CharField(max_length=20)
    program_code = models.CharField(max_length=20)
    days = models.CharField(max_length=100)
    time_in = models.TimeField()
    time_out = models.TimeField() 
        
    def __str__(self):
        return self.instructor_id