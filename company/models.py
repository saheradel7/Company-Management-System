from django.db import models


from django.db import models
from django.utils import timezone
from django.db.models import Count, F, Sum

class Company(models.Model):
    name = models.CharField(max_length=255, unique= True)

    def number_of_departments(self):
        return self.departments.count()

    def number_of_employees(self):
        return self.employees.count()

    def number_of_projects(self):
        return self.projects.count()

    def __str__(self):
        return self.name


class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def number_of_employees(self):
        return self.employees.count()

    def number_of_projects(self):
        return self.projects.count()

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)
    
    @property
    def days_employed(self):
        if self.hired_on:
            return (timezone.now().date() - self.hired_on).days
        return 0

    def __str__(self):
        return self.name


class Project(models.Model):
    company = models.ForeignKey(Company, related_name='projects', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name
