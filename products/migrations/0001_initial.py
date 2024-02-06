# Generated by Django 5.0.1 on 2024-02-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=13, unique=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lot', models.PositiveIntegerField()),
                ('production_date', models.DateField()),
                ('expiration_date', models.DateField()),
            ],
        ),
    ]
