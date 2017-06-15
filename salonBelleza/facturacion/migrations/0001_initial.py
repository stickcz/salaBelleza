# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='DetFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('idcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='detfactura',
            name='idfactura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Factura'),
        ),
        migrations.AddField(
            model_name='detfactura',
            name='idproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.Producto'),
        ),
    ]