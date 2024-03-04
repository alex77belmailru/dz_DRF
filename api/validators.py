from rest_framework import serializers


class QuantityValidator:
    """Класс валидации поля quantity"""

    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        quantity = dict(data).get(self.field)
        if quantity < 0:
            raise serializers.ValidationError('Недостаточно товара на складе')