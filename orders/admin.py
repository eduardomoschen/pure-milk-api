from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'seller', 'supermarket', 'date_of_order', 'invoicing')
    search_fields = ['seller__nome', 'supermarket__nome']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.calculate_invoicing()
        obj.save()

    def invoicing(self, obj):
        return obj.invoicing

    invoicing.short_description = 'Invoicing'
