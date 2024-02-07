from django.db import models


class Supermarket(models.Model):
    name = models.CharField(max_length=255)
    adress = models.TextField()
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def formatted_cnpj(self):
        return f'{self.cnpj[:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/\
{self.cnpj[8:12]}-{self.cnpj[12:]}'
    formatted_cnpj.short_description = 'CNPJ'

    def formatted_phone_number(self):
        if len(self.phone_number) == 10:
            return f'({self.phone_number[:2]}) {self.phone_number[2:6]}-\
{self.phone_number[6:]}'
        elif len(self.phone_number) == 11:
            return f'({self.phone_number[:2]}) {self.phone_number[2:7]}-\
{self.phone_number[7:]}'
        else:
            return self.phone_number
    formatted_phone_number.short_description = 'Phone Number'
