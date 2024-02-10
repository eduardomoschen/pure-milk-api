from django.db import models
from decimal import Decimal


class Seller(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_employment = models.DateField()
    employee = models.BooleanField(default=True)
    salary = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def calculate_commission_percentage(self):
        total_orders_value = self.orders.aggregate(models.Sum('invoicing'))['invoicing__sum'] or 0
        commission_percentage = total_orders_value * Decimal(0.02)
        self.salary = commission_percentage
        self.save()

    def formatted_phone_number(self):
        return f'({self.phone_number[:2]}) {self.phone_number[2:7]}-\
{self.phone_number[7:]}'

    def formatted_salary(self):
        return f'R$ {self.salary}'
