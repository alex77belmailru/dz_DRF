from django.contrib import admin

from api.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'position', 'is_active', 'is_staff', 'is_superuser',)
    list_editable = ('email', 'position', 'is_active', 'is_staff', 'is_superuser',)
    ordering = ('id',)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'storage')
    list_editable = ('name', 'quantity', 'storage')
    ordering = ('id',)
