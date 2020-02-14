from django.db import models

# Create your models here.

class studentsDetail(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    department=models.CharField(max_length=10)
    address=models.CharField(max_length=50)

