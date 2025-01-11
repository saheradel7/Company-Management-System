from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class UserRole(models.TextChoices):
    ADMIN = "admin", "Admin"
    MANAGER = "manager", "Manager"
    EMPLOYEE = "employee", "Employee"



class UserAccount(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices =UserRole.choices)

    def _str_(self):
        return self.user

# @receiver(post_save, sender=UserAccount)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance.user)
