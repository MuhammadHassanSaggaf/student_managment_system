from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Account
from student_managment_system.models import Student

def account_create(request):
    """
    Signup: create a Django User and link to an existing Student (by admission_number).
    """
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        admission_number = request.POST.get("admission_number", "").strip()
        password = request.POST.get("password", "").strip()

        if not (username and admission_number and password):
            messages.error(request, "All fields are required.")
            return render(request, "account_create.html")

        # Ensure student exists
        try:
            student = Student.objects.get(admission_number=admission_number)
        except Student.DoesNotExist:
            messages.error(request, "No student found with that admission number.")
            return render(request, "account_create.html")

        # Ensure username unique
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "account_create.html")

        # Ensure student doesn't already have an account
        if Account.objects.filter(student=student).exists():
            messages.error(request, "An account already exists for this student.")
            return render(request, "account_create.html")

        # Create user and set hashed password
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        # Link user to student via Account
        account = Account.objects.create(user=user, student=student)

        return render(request, "account_success.html", {"account": account})

    return render(request, "account_create.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                acct = Account.objects.select_related("student").get(user=user)
                admission = acct.student.admission_number
                return redirect('accounts:account_detail', admission_number=admission)
            except Account.DoesNotExist:
                return redirect('accounts:account_list')

        messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def account_detail_by_admission(request, admission_number):
    """
    Returns the Account (and student info) for a given admission_number.
    This view is good for students logging in to view their own data.
    """
    student = get_object_or_404(Student, admission_number=admission_number)
    try:
        account = Account.objects.get(student=student)
    except Account.DoesNotExist:
        account = None
    return render(request, "account_detail.html", {"student": student, "account": account})


def account_list(request):
    """
    Admin-style list of accounts.
    """
    accounts = Account.objects.select_related("user", "student").all().order_by("student__last_name")
    return render(request, "account_list.html", {"accounts": accounts})
