from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update data"""

    def has_object_permission(self, request, view, obj):
        """Check if user is valid to update data"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update own permissions only"""

    def has_object_permission(self, request, view, obj):
        """Check if user is valid to udpate status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id