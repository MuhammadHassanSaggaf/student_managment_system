from django.shortcuts import render,redirect

# Create your views here.
def list(request):
    return render(request, 'list.html')
  
def add(request):
    if request.method == 'POST':
        return redirect('list')  # Redirect to the list view after adding a student
    return render(request, 'add.html')  # Render the add student form template