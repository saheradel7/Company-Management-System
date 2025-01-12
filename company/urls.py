from django.urls import path,include
from .apis import (
    CompanyDetailView,
    CompanyListView,
    DepartmentDetailView,
    DepartmentListView,
    EmployeeDetailView,
    EmployeeListView,
    ProjectDetailView,
    ProjectListView
)


urlpatterns = [
    path('company/',CompanyListView.as_view(),name='company-list'),
    path('company/<int:pk>/',CompanyDetailView.as_view(),name='company-detail'),
    path('department/',DepartmentListView.as_view(),name='department-list'),
    path('department/<int:pk>/',DepartmentDetailView.as_view(),name='department-detail'),
    path('employee/',EmployeeListView.as_view(),name='employee-list'),
    path('employee/<int:pk>/',EmployeeDetailView.as_view(),name='employee-detail'),
    path('project/',ProjectListView.as_view(),name='project-list'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='project-detail'),
]
