from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from student_managment_system.models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET'])
def get_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.data)
  
@api_view(["DELETE"])
def delete_student(request, pk):
    student = Student.objects.get(id = pk)
    student.delete()
    return Response("Student Deleted Successfully", status=204)