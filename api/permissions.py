from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrReadOnly(BasePermission):
    """Проверка, что пользователь Админ, или вызван безопасный метод"""

    def has_permission(self, request, view):  # работает на уровне всего запроса
        if request.user.is_superuser:  # модератор имеет доступ ко всему
            return True

        return request.method in SAFE_METHODS


class IsOwner(BasePermission):
    """Проверка, что пользователь - владелец"""

    def has_object_permission(self, request, view, obj):  # работает на уровне отдельно объекта бд
        return request.user == obj
