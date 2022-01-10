from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пермишен, дающий полный доступ к объекту только его автору.
    Безопасные запросы доступны любому пользователю.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
