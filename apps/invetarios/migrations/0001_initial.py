# Generated by Django 4.2.4 on 2023-12-05 22:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventarioStock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('entrada_kg', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('entrada_cm', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('salida_kg', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('salida_cm', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock_kg', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stock_cm', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ponderado_stock', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
