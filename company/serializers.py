from rest_framework.serializers import ModelSerializer
from .models import Company , Department , Employee , Project

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
