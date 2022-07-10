# Generated by Django 4.0.6 on 2022-07-10 14:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Delifrus', '0002_remove_marca_favicon_amarillo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasif_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion_producto', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'verbose_name_plural': 'PROD- 01. Clasificación de Producto',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(blank=True, max_length=100, null=True)),
                ('stock', models.CharField(choices=[('stock', 'stock'), ('no_stock', 'no_stock')], default='stock', max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='producto/')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('caracteristicas', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('tamanos', models.TextField(blank=True, max_length=500, null=True)),
                ('material', models.TextField(blank=True, max_length=500, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('clasif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Delifrus.clasif_producto')),
            ],
            options={
                'verbose_name_plural': 'PROD- 02. Producto',
            },
        ),
        migrations.CreateModel(
            name='Producto_Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galeria_articulo', models.ImageField(blank=True, help_text='imagen producto 800x800', null=True, upload_to='media')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Delifrus.producto')),
            ],
            options={
                'verbose_name_plural': 'PROD- 03. Producto Imagenes',
            },
        ),
    ]