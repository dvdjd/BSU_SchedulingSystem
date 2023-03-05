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
    subject_code = models.ForeignKey(SubjectModel,on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel,on_delete=models.CASCADE)
    days = models.CharField(max_length=100)
    time_in = models.TimeField()
    time_out = models.TimeField() 
        
    def __str__(self):
        return self.instructor_id