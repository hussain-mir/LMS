from django.urls import path
from . import views

urlpatterns = [
    path('teacher_signup', views.teacher_signup, name='teacher_signup'),
    path('teacher_login', views.teacher_login, name='teacher_login'),
    path('teacher_logout', views.teacher_logout, name='teacher_logout'),
    path('submitquestions', views.submit_questions, name='submit_questions'),
    path('teacherdashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacherlecturescreen', views.teacher_lecture_screen, name='teacher_lecture_screen'),
    
]
