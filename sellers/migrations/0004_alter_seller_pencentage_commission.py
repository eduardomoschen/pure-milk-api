# Generated by Django 5.0.1 on 2024-02-08 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_seller_pencentage_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='pencentage_commission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
