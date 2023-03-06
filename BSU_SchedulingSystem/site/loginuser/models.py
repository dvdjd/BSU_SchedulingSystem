from django.db import models

USER_TYPE = (
    ('student', 'Student'),
    ('instructor', 'Instructor'),
    ('admin', 'Administrator'),
)

class LoginUser(models.Model):
    
    userid = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    usertype = models.CharField(max_length=20, choices=USER_TYPE, default='Select User Type')
    
    def __str__(self):
        return self.username
    
