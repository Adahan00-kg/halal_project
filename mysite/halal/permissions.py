from rest_framework import permissions


class CheckNotesOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False



