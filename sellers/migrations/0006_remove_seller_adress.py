# Generated by Django 5.0.1 on 2024-02-10 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0005_rename_pencentage_commission_seller_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='adress',
        ),
    ]
