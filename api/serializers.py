from rest_framework import serializers
from student_managment_system.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['id', 'first_name', 'last_name', 'admission_number', 'date_of_birth', 'enrollment_date', 'course_taken', 'gender'] #This is useful for specific fields otherwise use fields = '__all__' like i used below
        fields = '__all__'