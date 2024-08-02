# Generated by Django 5.0.7 on 2024-08-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1', models.CharField(max_length=100)),
                ('nombre2', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('fecha_egreso', models.DateField(blank=True, null=True, verbose_name='Salida')),
            ],
        ),
    ]
