from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    center_code = models.CharField(max_length=10, unique=True)
    center_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    
    def __str__(self):
        return self.center_name
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()


class Exam(models.Model):
    exam_code = models.CharField(max_length=10, unique=True)
    exam_title = models.CharField(max_length=100)
    center_code = models.CharField(max_length=10, unique=True)
    center_name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    date = models.DateField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.exam_title

class HallTicket(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f"Hall Ticket for {self.student.user.username} - {self.exam.exam_title}"

    