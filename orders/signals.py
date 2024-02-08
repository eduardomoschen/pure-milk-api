from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, OrderItem

@receiver(post_save, sender=OrderItem)
def calculate_invoicing_on_orderitem_save(sender, instance, **kwargs):
    instance.order.calculate_invoicing()
    instance.order.save()
