from django.db import models
from room.models import RoomModel
from curriculum.models import SubjectModel

# Create your models here.
class ExamModel(models.Model):

    subject_code = models.ForeignKey(SubjectModel,on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel,on_delete=models.CASCADE)
    days = models.CharField(max_length=100)
    time_in = models.TimeField()
    time_out = models.TimeField() 
