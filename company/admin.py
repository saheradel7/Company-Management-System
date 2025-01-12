from django.contrib import admin
from .models import Company, Department, Employee, Project


class CompanyAdmin(admin.ModelAdmin):

    list_display = ['name', 'number_of_departments','number_of_employees','number_of_projects']
    readonly_fields = ['number_of_departments','number_of_employees','number_of_projects']

    def number_of_departments(self, obj):
        return obj.departments.count()
    number_of_departments.short_description = 'number of departments'

    def number_of_employees(self, obj):
        return obj.employees.count()
    number_of_employees.short_description = 'number of employees'

    def number_of_projects(self, obj):
        return obj.projects.count()    
    number_of_projects.short_description = 'number of projects'

admin.site.register(Company, CompanyAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','company' , 'number_of_employees','number_of_projects']

    def number_of_employees(self, obj):
        return obj.employees.count()
    
    def number_of_projects(self, obj):
        return obj.projects.count()
    
admin.site.register(Department, DepartmentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'company',
        'department',
        'name',
        'email',
        'mobile_number',
        'address',
        'designation',
        'hired_on'
    ]
admin.site.register(Employee, DepartmentAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'company',
        'department',
        'name',
        'description',
        'start_date',
        'end_date',
    ]

admin.site.register(Project, ProjectAdmin)
