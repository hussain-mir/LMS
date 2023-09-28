from django.contrib.auth.models import AbstractUser
from django.db import models
    
class User(AbstractUser):
    isTeacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Questions(models.Model):
    student_question=models.CharField(max_length=300)
    teacher_question=models.CharField(max_length=300)
    teacher_answer=models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # id = models.AutoField(primary_key=True)

    # def __str__(self):
    #     return f"Question by {self.timestamp} "