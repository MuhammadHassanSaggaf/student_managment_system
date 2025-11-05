from django.shortcuts import render,redirect

# Create your views here.
def list(request):
    return render(request, 'list.html')
  
def add(request):
    if request.method == 'POST':
        return redirect('list')  # Redirect to the list view after adding a student
    return render(request, 'add.html')  # Render the add student form template
  
def edit(request, student_id):
    if request.method == 'POST':
        return redirect('list')  # Redirect to the list view after editing a student
    # Here you would typically fetch the student by ID and pass it to the template
    student = None  # Replace with actual student fetching logic
    return render(request, 'edit.html', {'student': student})  # Render the edit student form template