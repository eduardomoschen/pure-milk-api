from django.db import models
from products.models import Product
from sellers.models import Seller
from supermarkets.models import Supermarket


class Order(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.PROTECT)
    date_of_order = models.DateField(auto_now_add=True)
    invoicing = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.id} - {self.seller} - {self.supermarket}: {self.date_of_order}'

    def calculate_invoicing(self):
        total_invoicing = sum(item.calculate_item_invoicing() for item in self.order_items.all())
        self.invoicing = total_invoicing

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.calculate_invoicing()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def calculate_item_invoicing(self):
        return self.product.value * self.quantity
