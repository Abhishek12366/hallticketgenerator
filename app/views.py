from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework import viewsets

# Create your views here.

class HallTicketViewSet(viewsets.ModelViewSet):
    queryset = HallTicket.objects.all()
    serializer_class = HallTicketSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
