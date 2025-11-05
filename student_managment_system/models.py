from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    class Gender(models.TextChoices):
      MALE = 'Male', 'Male'
      FEMALE = 'Female', 'Female'
      OTHER = 'Other', 'Other'
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)
    course_taken = models.CharField(max_length=100)
    gender = models.CharField(choices =(Gender.choices),)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"