from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=25)
    uname =  models.CharField(max_length = 40)
    pwd = models.CharField(max_length = 25)
    pwd2 = models.CharField(max_length = 25)
    
    
    
