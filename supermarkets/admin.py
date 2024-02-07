from django.contrib import admin
from .models import Supermarket


@admin.register(Supermarket)
class SupermarketAdmin(admin.ModelAdmin):
    ...
