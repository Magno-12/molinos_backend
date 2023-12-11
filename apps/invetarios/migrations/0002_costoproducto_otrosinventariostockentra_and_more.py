# Generated by Django 4.2.4 on 2023-12-11 18:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invetarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoProducto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('referencia', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_por_kg', models.DecimalField(decimal_places=2, max_digits=15)),
                ('factura_compra', models.CharField(max_length=50)),
                ('fecha_actualizacion', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtrosInventarioStockEntra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('longitud_cm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateField()),
                ('entrada_kls', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ponderado_compra', models.DecimalField(decimal_places=2, max_digits=15)),
                ('factura_compra', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PedidoMateriaPrima',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('proveedor', models.CharField(max_length=255)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('producto', models.CharField(max_length=255)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrecioProveedorPorAno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('ano', models.IntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=15)),
                ('proveedor', models.CharField(max_length=255)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precios_proveedores', to='invetarios.costoproducto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
