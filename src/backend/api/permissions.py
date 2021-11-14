'''
Created on May 25, 2018

@author: kjnether
'''
from rest_framework.permissions import BasePermission
from .models import ReplicationJobs

class IsOwner(BasePermission):
    """Custom permission class to allow only job owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, ReplicationJobs):
            return obj.owner == request.user
        return obj.owner == request.user