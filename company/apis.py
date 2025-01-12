from rest_framework import generics 
from .models import Company , Department , Employee , Project
from .serializers import CompanySerializer , DepartmentSerializer , EmployeeSerializer , ProjectSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import (
    ManagerPermission,
    AdminPermission,
    EmployeePermission
)

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]



class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]


class DepartmentListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]

class DepartmentDetailView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer   
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ManagerPermission | AdminPermission| EmployeePermission] 
    authentication_classes = [TokenAuthentication]
