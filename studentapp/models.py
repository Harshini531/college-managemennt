from django.db import models
from django.db.models import CASCADE

class Place(models.Model):
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Student(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    MobileNumber=models.BigIntegerField()
    Place = models.ForeignKey(Place,on_delete=models.CASCADE)