from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from api_user.models import UserAccount , UserRole

class ManagerPermission(BasePermission):
    def has_permission(self, request: Request, view):
        user = UserAccount.objects.get(user=request.user)
        return bool(
            user.role == UserRole.MANAGER
        )


class AdminPermission(BasePermission):
    def has_permission(self, request: Request, view):
        user = UserAccount.objects.get(user=request.user)
        return bool(
            user.role == UserRole.ADMIN
        )

class EmployeePermission(BasePermission):
    def has_permission(self, request: Request, view):
        user = UserAccount.objects.get(user=request.user)
        return bool(
            user.role == UserRole.EMPLOYEE
        )
