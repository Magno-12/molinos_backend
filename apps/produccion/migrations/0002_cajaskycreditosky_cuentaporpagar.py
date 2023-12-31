# Generated by Django 4.2.4 on 2023-12-11 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CajaSkyCreditoSky',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('fecha', models.DateField()),
                ('cliente', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('valor_negocio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('recibo', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CuentaPorPagar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('nombre_proveedor', models.CharField(max_length=255)),
                ('cedula_nit', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fv_rc_rem', models.CharField(max_length=50)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('centro_costos', models.CharField(max_length=255)),
                ('medio_pago', models.CharField(max_length=50)),
                ('valor_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_bruto', models.DecimalField(decimal_places=2, max_digits=15)),
                ('abonos', models.DecimalField(decimal_places=2, max_digits=15)),
                ('fecha_abonos', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
