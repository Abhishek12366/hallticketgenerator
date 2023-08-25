"""hallticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import*



router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'halltickets', HallTicketViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
     path('', include(router.urls)),
     path('student_info/', student_info, name='student_info'),
    path('exam_selection/', exam_selection, name='exam_selection'),
    path('hall_ticket_display/',hall_ticket_display, name='hall_ticket_display'),
]
