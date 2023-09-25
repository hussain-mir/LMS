from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions

from student.models import User


# Create your views here.


def index(request):
    return render(request, "index.html")

@csrf_exempt
def student_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, 'A student with this email already exists.')
            else:
                user = User.objects.create(
                    username=email,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                user.set_password(password)
                user.isTeacher = False
                user.save()
                login(request, user)
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'Student_Signup.html')

@csrf_exempt
def login_student(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            error_message = "Invalid email or password."

    return render(request, 'Login_page_Student.html', {'error_message': error_message})


def student_logout_view(request):
    logout(request)
    return redirect('login_student')


def student_dashboard(request):
    return render(request, "student_dashboard.html")


def student_lecture_screen(request):
    
    if request.method == 'POST':
        student_question = request.POST.get('student_question')
        ins=Questions(student_question=student_question)
        ins.save()
        print(student_question)
    
    return render(request, "student_lecture_screen.html")
