from django.contrib import admin
from django.urls import path
from .apis import RegisterView,LoginView

urlpatterns = [
    path('register' , RegisterView.as_view(),name='register'),
    path('login' , LoginView.as_view(),name='loin')

]
