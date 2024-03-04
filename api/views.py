from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from api.models import *
from api.permissions import *
from api.serializers import *


class UserModelViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с классом Пользователь"""
    queryset = User.objects.all()
    permission_classes = [IsOwner | IsAdminUser]

    def get_serializer_class(self, **kwargs):
        """Выбор сериализатора в зависимости от запроса"""
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer


class StorageModelViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с классом Склад"""

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [AdminOrReadOnly]


class ProductModelViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с классом Товар"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        """Вызывается при изменении товара"""
        product_to_change = Product.objects.get(pk=kwargs['pk'])  # изменяемый товар
        entered_quantity = int(request.data['quantity'])  # введенное количество товара

        # # Попытка ввести отрицательное количество товара
        # if entered_quantity < 0:
        #     raise serializers.ValidationError('Недостаточно товара на складе')

        # Поставщик, не может получать товар
        if request.user.position == 'provider' and entered_quantity < product_to_change.quantity:
            raise serializers.ValidationError('Текущий пользователь - Поставщик, не может получать товар')

        # Потребитель не может поставлять товар и менять склад товара
        if request.user.position == 'consumer':
            if entered_quantity > product_to_change.quantity:
                raise serializers.ValidationError('Текущий пользователь - Потребитель, не может поставлять товар')
            if int(request.data['storage']) != product_to_change.storage.pk:
                raise serializers.ValidationError('Текущий пользователь - Потребитель, не может менять склад')

        # Менять название товара может только суперюзер
        if not request.user.is_superuser and product_to_change.name != request.data['name']:
            raise serializers.ValidationError('Нет прав на изменение товара')

        return super().update(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        # Удалять товар может только суперюзер
        if not request.user.is_superuser:
            raise serializers.ValidationError('Нет прав на удаление товара')
        return super().destroy(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        # Создавать товар может только суперюзер
        if not request.user.is_superuser:
            raise serializers.ValidationError('Нет прав на создание товара')
        return super().create(request, *args, **kwargs)