from rest_framework import serializers

from api.models import *
from api.validators import QuantityValidator


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор, используемый при создании юзера"""

    class Meta:
        model = User
        fields = ('id', 'email', 'position', 'password')

    def save(self, **kwargs):
        password = self.validated_data['password']
        user = User.objects.create(
            email=self.validated_data.get('email'),
            position=self.validated_data.get('position'),
        )
        user.set_password(password)  # хэширует пароль для хранения в бд
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для методов кроме создания юзера"""

    class Meta:
        model = User
        fields = ('id', 'email', 'position')


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'storage')
        validators = [QuantityValidator(field='quantity')]

# вариант из лекции
# class UserSerializer(serializers.Serializer):
#     email = serializers.EmailField(validators=[
#         validators.UniqueValidator(User.objects.all())
#     ])
#     position = serializers.ChoiceField(choices=Positions.choices)
#     password = serializers.CharField(min_length=6, max_length=20, write_only=True)
#
#     def update(self, instance, validated_data):
#         if email := validated_data.get("email"):
#             instance.email = email
#             instance.save(update_fields=["email"])
#
#         if password := validated_data.get("password"):
#             instance.set_password(password)
#             instance.save(update_fields=["password"])
#
#         if position := validated_data.get("position"):
#             instance.position=position
#             instance.save(update_fields=["position"])
#         return instance
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             email=validated_data["email"],
#             position=validated_data["position"],
#         )
#
#         user.set_password(validated_data["password"])
#         user.save(update_fields=["password"])
#         return user
