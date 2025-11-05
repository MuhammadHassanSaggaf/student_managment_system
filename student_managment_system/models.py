from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField(auto_now_add=True)
    course_taken = models.CharField(max_length=100)
    gender = models.CharField(choices =("Male", "Female", "Other"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"