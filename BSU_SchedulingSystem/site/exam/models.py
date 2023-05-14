from django.db import models
from room.models import RoomModel
from curriculum.models import SubjectModel

# Create your models here.
class ExamModel(models.Model):

    subject_code = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10)
    section_code = models.CharField(max_length=10)
    instructor_id  = models.CharField(max_length=20)
    room = models.CharField(max_length=20)
    days = models.CharField(max_length=100)
    time_in = models.TimeField()
    time_out = models.TimeField()
