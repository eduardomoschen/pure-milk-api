from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from orders.models import Order


@receiver(post_save, sender=Order)
@receiver(post_delete, sender=Order)
def update_seller_comission(sender, instance, **kwargs):
    seller = instance.seller
    seller.calculate_commission_percentage()
