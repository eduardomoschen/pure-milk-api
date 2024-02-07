from django.core.files.base import ContentFile
from django.db import models
from datetime import timedelta
from faker import Faker
from barcode import EAN13
from barcode.writer import ImageWriter
from io import BytesIO
import os

fake = Faker()


class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=13, unique=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    lot = models.PositiveIntegerField(blank=True, null=True)
    production_date = models.DateField(blank=True)
    expiration_date = models.DateField(blank=True)
    barcode_image = models.ImageField(upload_to='products/barcodes', blank=True)

    def generate_barcode(self):
        if not self.barcode:
            barcode_value = fake.ean13()

            ean = EAN13(barcode_value, writer=ImageWriter())

            image_bytes_io = BytesIO()
            ean.write(image_bytes_io)
            image_bytes_io.seek(0)

            barcode_path = os.path.join(f'{self.name.lower()}.png')

            image_content = ContentFile(
                image_bytes_io.read(),
                name=barcode_path
            )

            self.barcode = barcode_value
            self.barcode_image.save(barcode_path, image_content)

    def set_expiration_date(self):
        product_name = self.name

        print(f"Product Name: {product_name}")

        if self.name in ['Leite A2', 'Leite A2 Zero Lactose']:
            self.expiration_date = self.production_date + timedelta(days=14)
        elif self.name == 'Leite A2 Fermentado':
            self.expiration_date = self.production_date + timedelta(days=30)
        elif self.name in [
            'Bebida Láctea de Ameixa',
            'Bebida Láctea de Morango',
            'Bebida Láctea de Graviola'
        ]:
            self.expiration_date = self.production_date + timedelta(days=60)
        elif self.name in [
            'Coalhada Tradicional',
            'Coalhada Light',
            'Coalhada Natural A2',
            'Coalhada Zero Lactose',
            'Coalhada de Ameixa',
            'Coalhadade Morango',
            'Iogurte Desnatado',
            'Iogurte Integral',
            'Iogurte de Morango'
        ]:
            self.expiration_date = self.production_date + timedelta(days=90)
        elif self.name in [
            'Requeijão Cremoso Tradicional',
            'Requeijão Cremoso Light',
            'Requeijão Cremoso Zero Lactose'
        ]:
            self.expiration_date = self.production_date + timedelta(days=120)

    def save(self, *args, **kwargs):
        self.set_expiration_date()
        self.generate_barcode()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
