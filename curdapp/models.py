from django.db import models

# Create your models here.
from django.urls import reverse


class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    roll_number=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=4)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_list', kwargs={'pk': self.id})
