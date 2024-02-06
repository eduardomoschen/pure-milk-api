from django.db import models


class Seller(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    adress = models.TextField(blank=True)
    date_of_employment = models.DateField()
    employee = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
