# Generated by Django 5.0.1 on 2024-02-08 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0004_alter_seller_pencentage_commission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='pencentage_commission',
            new_name='salary',
        ),
    ]
