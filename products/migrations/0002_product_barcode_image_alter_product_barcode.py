# Generated by Django 5.0.1 on 2024-02-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode_image',
            field=models.ImageField(blank=True, upload_to='barcodes/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=13, unique=True),
        ),
    ]