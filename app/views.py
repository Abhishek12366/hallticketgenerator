from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework import viewsets

# Create your views here.


def index(request):
    return render(request, 'index.html')

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


def student_info(request):
    return render(request, 'student_form.html')

def exam_selection(request):
    return render(request, 'exam_form.html')

def hall_ticket_display(request):
    return render(request, 'hall_ticket.html')



### test +++++]]
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Admin, AdminRequest
# from .serializers import AdminSerializer, AdminRequestSerializer
# from .permissions import IsSuperAdmin
# from django.contrib import messages
# from django.contrib.auth.views import LoginView
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# class SuperAdminLoginView(LoginView):
#     template_name = 'superadmin_login.html'  # Replace with your template path

#     def form_valid(self, form):
#         if self.request.user.is_superuser:
#             return super().form_valid(form)
#         else:
#             messages.error(self.request, "You are not authorized as a superadmin.")
#             return HttpResponseRedirect(reverse('superadmin_login'))



# class AdminRequestViewSet(viewsets.ModelViewSet):
#     queryset = AdminRequest.objects.all()
#     serializer_class = AdminRequestSerializer

#     @action(detail=True, methods=['POST'])
#     def accept_request(self, request, pk=None):
#         admin_request = self.get_object()
#         if admin_request.is_accepted:
#             return Response({'detail': 'Request has already been accepted.'}, status=400)
       
#         admin = Admin.objects.create_user(
#             username=admin_request.email,
#             email=admin_request.email,
#             password=admin_request.password,
#         )
#         admin_request.is_accepted = True
#         admin_request.save()
#         return Response({'detail': 'Request accepted and admin created successfully.'})

# class AdminViewSet(viewsets.ModelViewSet):
#     queryset = Admin.objects.all()
#     serializer_class = AdminSerializer





# class AdminRequestViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsSuperAdmin]
    

# class AdminViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsSuperAdmin]