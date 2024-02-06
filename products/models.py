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

            barcode_path = os.path.join(f'{self.name}.png')

            image_content = ContentFile(
                image_bytes_io.read(),
                name=barcode_path
            )

            self.barcode = barcode_value
            self.barcode_image.save(barcode_path, image_content)

    def set_expiration_date(self):
        if self.name.lower() == ['Leite A2', 'Leite A2 Zero Lactose']:
            self.expiration_date = self.production_date + timedelta(days=14)
        elif self.name.lower() == 'Leite A2 Fermentado':
            self.expiration_date = self.production_date + timedelta(days=30)
        elif self.name.lower() == [
            'Coalhada Tradicional',
            'Coalhada Light',
            'Coalhada Natural A2',
            'Coalhada Zero Lactose',
            'Coalhada de Ameixa',
            'Coalhadade Morango',
            'Iogurte Desnatado',
            'Iogurte Integral',
            'Iogurte de Morango',
            'Bebida Láctea de Ameixa',
            'Bebida Láctea de Morango',
            'Bebida Láctea de Graviola'
        ]:
            self.expiration_date = self.production_date + timedelta(days=90)
        elif self.nome.lower() == [
            'Requeijão Cremoso Tradicional',
            'Requeijão Cremoso Light',
            'Requeijão Cremoso Zero Lactose'
        ]:
            self.expiration_date = self.production_date + timedelta(days=120)

    def save(self, *args, **kwargs):
        self.generate_barcode()
        self.set_expiration_date()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
