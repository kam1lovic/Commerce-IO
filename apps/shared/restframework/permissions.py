from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsOwnerShop(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner') and obj.owner == request.user:
            return True
        raise PermissionDenied({'detail': 'You do not own this object.'})


class IsOwnerCategory(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.shop == request.user.default_shop:
            return super().has_object_permission(request, view, obj)
        raise PermissionDenied({'detail': 'You do not own this object or shop does not match.'})
