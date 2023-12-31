
from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # to the check logigedin admin is  SuperAdmin or not
        return request.user.is_authenticated and request.user.is_superuser
