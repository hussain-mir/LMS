from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


from student.models import User

# Create your views here.

@csrf_exempt
def teacher_signup(request):
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
                user.isTeacher = True
                user.save()
                login(request, user)
                return redirect('teacher_dashboard')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request,"Teacher_Signup.html")

@csrf_exempt
def teacher_login(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST.get('emailaddress').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        print(user.isTeacher)

        if user is not None and user.isTeacher == True:
            login(request, user)
            return redirect('teacher_dashboard')
        else:
            error_message = "Invalid email or password."

    return render(request, 'Login_page_Teacher.html', {'error_message': error_message})

@csrf_exempt
def teacher_logout(request):
    logout(request)
    return redirect('teacher_login')

def submit_questions(request):
    return render(request,"submit_questions.html")

def teacher_dashboard(request):
    return render(request,"teacher_dashboard.html")

def teacher_lecture_screen(request):
    return render(request,"teacher_lecture_screen.html")
