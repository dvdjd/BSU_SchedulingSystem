from django.db import models

# Create your models here.
class RoomModel(models.Model):
    
    room = models.CharField(max_length=20)
        
    def __str__(self):
        return self.room