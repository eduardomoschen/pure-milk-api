# Generated by Django 5.0.1 on 2024-02-08 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_invoicing'),
        ('sellers', '0004_alter_seller_pencentage_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='sellers.seller'),
        ),
    ]
