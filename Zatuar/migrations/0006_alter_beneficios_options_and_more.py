# Generated by Django 4.0.6 on 2022-07-10 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Zatuar', '0005_alter_slider_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficios',
            options={'verbose_name_plural': '5. Zatuar Beneficios'},
        ),
        migrations.AlterModelOptions(
            name='clasif_producto',
            options={'verbose_name_plural': '9.3. Clasificaciòn de Producto'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': '9.9. Clientes'},
        ),
        migrations.AlterModelOptions(
            name='descarga',
            options={'verbose_name_plural': '9.2. Descarga'},
        ),
        migrations.AlterModelOptions(
            name='detalles',
            options={'verbose_name_plural': '9.1. Detalles'},
        ),
        migrations.AlterModelOptions(
            name='galeria_cliente',
            options={'verbose_name_plural': '9.9.1 Cliente Galeria'},
        ),
        migrations.AlterModelOptions(
            name='galeria_proceso',
            options={'verbose_name_plural': '9. Galeria_Proceso'},
        ),
        migrations.AlterModelOptions(
            name='identidad',
            options={'verbose_name_plural': '7. Zatuar es'},
        ),
        migrations.AlterModelOptions(
            name='personalizaion_poducto',
            options={'verbose_name_plural': '6. Perzonalizacion de Productos'},
        ),
        migrations.AlterModelOptions(
            name='proceso',
            options={'verbose_name_plural': '8. Proceso'},
        ),
        migrations.AlterModelOptions(
            name='producto_cliente',
            options={'verbose_name_plural': '9.9.2 Mandil Cliente'},
        ),
        migrations.AlterModelOptions(
            name='producto_imagen',
            options={'verbose_name_plural': '9.6. Producto Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='producto_personalizacion',
            options={'verbose_name_plural': '9.7. Producto Personalizacion'},
        ),
        migrations.AlterModelOptions(
            name='producto_slider',
            options={'verbose_name_plural': '9.8. Slider'},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='slug',
        ),
    ]
