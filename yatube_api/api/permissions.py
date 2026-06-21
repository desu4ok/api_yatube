from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее только автору редактировать или удалять контент.
    Для остальных пользователей доступен только просмотр (SAFE_METHODS).
    """

    def has_permission(self, request, view):
        # Общая проверка: читать могут все, а вот создавать/менять
        # только авторизованные пользователи
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
