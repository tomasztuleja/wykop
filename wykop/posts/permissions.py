from datetime import timedelta

from django.utils import timezone
from rest_framework import permissions


class PostPermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        now = timezone.now()
        half_hour_ago = now - timedelta(minutes=30)
        
        return obj.author == request.user and obj.created > half_hour_ago
