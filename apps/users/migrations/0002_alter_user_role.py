# Generated by Django 4.2.4 on 2023-12-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'admin'), ('customer', 'customer')], max_length=50, null=True),
        ),
    ]