from django.contrib.auth.models import AbstractUser
from django.db import models


class Positions(models.TextChoices):
    provider = 'provider'
    consumer = 'consumer'


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    position = models.CharField(max_length=20, verbose_name='Должность', choices=Positions.choices,
                                null=False, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Storage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Склад: {self.name}"

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Наименование')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    storage = models.ForeignKey(Storage, related_name="product", verbose_name='Склад',
                                on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Товар:{self.name}, количество: {self.quantity}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
