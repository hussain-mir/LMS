from django.urls import path

from student import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('student_lecture_screen', views.student_lecture_screen,
         name='student_lecture_screen'),
    path('student_signup', views.student_signup, name='Student_Signup'),
    path('login_student', views.login_student, name='login_student'),
    path('student/logout/', views.student_logout_view, name='student_logout'),
]
