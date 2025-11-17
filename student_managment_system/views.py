from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
# Create your views here.
def list(request):
    students = Student.objects.all().order_by('last_name', 'first_name')
    return render(request, 'list.html', {'students': students})
  
def add(request):
    if request.method == 'POST':
        Student.objects.create(
            admission_number = request.POST["admission_number"],
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"],
            date_of_birth = request.POST["date_of_birth"],    # YYYY-MM-DD
            course_taken = request.POST["course_taken"],
            gender = request.POST["gender"],                 # "Male"/"Female"/"Other"
        )
        return redirect("student_managment_system:list")  # Redirect to the list view after adding a student
    return render(request, 'add.html')  # Render the add student form template
  
def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    errors = []

    if request.method == "POST":
        admission_number = request.POST.get("admission_number", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        date_of_birth = request.POST.get("date_of_birth", "").strip()
        course_taken = request.POST.get("course_taken", "").strip()
        gender = request.POST.get("gender", "").strip()

        # Basic server-side validation
        if not (admission_number and first_name and last_name and date_of_birth and course_taken and gender):
            errors.append("All fields are required.")
        else:
            # If admission number changed, ensure uniqueness
            if admission_number != student.admission_number and Student.objects.filter(admission_number=admission_number).exists():
                errors.append("A different student with that admission number already exists.")
            else:
                # Save updated values
                student.admission_number = admission_number
                student.first_name = first_name
                student.last_name = last_name
                student.date_of_birth = date_of_birth
                student.course_taken = course_taken
                student.gender = gender
                student.save()
                return redirect("student_managment_system:list")

    # GET or validation errors -> render edit form prefilled
    return render(request,
                  "edit.html",
                  {
                      "student": student,
                      "errors": errors,
                  })
    
def delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect("student_managment_system:list")