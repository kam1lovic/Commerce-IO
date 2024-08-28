from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner') and obj.owner == request.user:
            return True
        if hasattr(obj, 'shop') and obj.shop == request.user.default_shop:
            return True
        raise PermissionDenied({'detail': 'You do not own this object or shop does not match.'})
