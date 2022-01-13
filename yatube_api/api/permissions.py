from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsReadOnly(ReadOnly):
    """
    Безопасные запросы доступны любому пользователю.
    """

    def has_object_permission(self, request, view, obj):
        return super().has_permission(request, view)


class IsAuthor(BasePermission):
    """
    Пермишен, дающий полный доступ к объекту только его автору.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
