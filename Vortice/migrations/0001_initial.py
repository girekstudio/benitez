# Generated by Django 4.0.6 on 2022-07-06 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '4. Articulo ',
            },
        ),
        migrations.CreateModel(
            name='Camiseta_Imagen_detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_cuello_o', models.ImageField(blank=True, help_text='500x500', null=True, upload_to='media')),
                ('detalle_cuello_o', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_cuello_v_hombre', models.ImageField(blank=True, help_text='500x500', null=True, upload_to='media')),
                ('detalle_cuello_v_hombre', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_cuello_v_mujer', models.ImageField(blank=True, help_text='500x500', null=True, upload_to='media')),
                ('detalle_cuello_v_mujer', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '3. Camiseta_Imagen_detalle ',
            },
        ),
        migrations.CreateModel(
            name='Camiseta_talla_Hombre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuello_redondo', models.BooleanField(default=False)),
                ('cuello_v', models.BooleanField(default=False)),
                ('talla', models.CharField(blank=True, max_length=2, null=True)),
                ('espalda', models.CharField(blank=True, max_length=2, null=True)),
                ('ancho', models.CharField(blank=True, max_length=2, null=True)),
                ('alto', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name_plural': '6. Camiseta_talla_Hombre ',
            },
        ),
        migrations.CreateModel(
            name='Camiseta_talla_Mujer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuello_redondo', models.BooleanField(default=False)),
                ('cuello_v', models.BooleanField(default=False)),
                ('talla', models.CharField(blank=True, max_length=2, null=True)),
                ('espalda', models.CharField(blank=True, max_length=2, null=True)),
                ('ancho', models.CharField(blank=True, max_length=2, null=True)),
                ('alto', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name_plural': '6. Camiseta_talla_Mujer ',
            },
        ),
        migrations.CreateModel(
            name='Camiseta_talla_Nena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuello_redondo', models.BooleanField(default=False)),
                ('cuello_v', models.BooleanField(default=False)),
                ('talla', models.CharField(blank=True, max_length=2, null=True)),
                ('espalda', models.CharField(blank=True, max_length=2, null=True)),
                ('ancho', models.CharField(blank=True, max_length=2, null=True)),
                ('alto', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name_plural': '6. Camiseta talla Nena ',
            },
        ),
        migrations.CreateModel(
            name='Camiseta_talla_Nene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuello_redondo', models.BooleanField(default=False)),
                ('cuello_v', models.BooleanField(default=False)),
                ('talla', models.CharField(blank=True, max_length=2, null=True)),
                ('espalda', models.CharField(blank=True, max_length=2, null=True)),
                ('ancho', models.CharField(blank=True, max_length=2, null=True)),
                ('alto', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name_plural': '6. Camiseta talla Nene ',
            },
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.BooleanField(default=False)),
                ('nuevo', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=False)),
                ('tema', models.CharField(blank=True, max_length=30, null=True)),
                ('imagen', models.FileField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('portada', models.FileField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('icono', models.FileField(blank=True, help_text='100x100', null=True, upload_to='media')),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': '2. Coleccion ',
            },
        ),
        migrations.CreateModel(
            name='Contacto_redes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('ticktock', models.CharField(blank=True, max_length=100, null=True)),
                ('behance', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '8. Contácto Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='Imag_prenda_articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=30, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='100x100', null=True, upload_to='media')),
            ],
            options={
                'verbose_name_plural': '3. Imag_prenda_articulo ',
            },
        ),
        migrations.CreateModel(
            name='Muestra_productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_1', models.ImageField(blank=True, help_text='imagenes 504*250', null=True, upload_to='media')),
                ('titulo_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_titulo_1', models.CharField(blank=True, max_length=100, null=True)),
                ('link_1', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_2', models.ImageField(blank=True, help_text='imagenes 250*250', null=True, upload_to='media')),
                ('titulo_2', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_titulo_2', models.CharField(blank=True, max_length=100, null=True)),
                ('link_2', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_3', models.ImageField(blank=True, help_text='imagenes 250*250', null=True, upload_to='media')),
                ('titulo_3', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_titulo_3', models.CharField(blank=True, max_length=100, null=True)),
                ('link_3', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_4', models.ImageField(blank=True, help_text='imagenes 504*250', null=True, upload_to='media')),
                ('titulo_4', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_titulo_4', models.CharField(blank=True, max_length=100, null=True)),
                ('link_4', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_5', models.ImageField(blank=True, help_text='imagenes 504*500', null=True, upload_to='media')),
                ('titulo_5', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_titulo_5', models.CharField(blank=True, max_length=100, null=True)),
                ('link_5', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '3. Galeria productos Imagenes',
            },
        ),
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_visible', models.BooleanField(default=False)),
                ('articulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.articulo')),
                ('coleccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.coleccion')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.imag_prenda_articulo')),
            ],
            options={
                'verbose_name_plural': '5. Prenda ',
            },
        ),
        migrations.CreateModel(
            name='Seccion_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(blank=True, max_length=30, null=True)),
                ('icono', models.FileField(blank=True, help_text='cuadrada', null=True, upload_to='cliente')),
                ('imagen_vertical', models.FileField(blank=True, help_text='vertical', null=True, upload_to='cliente')),
                ('imagen_horizontal', models.FileField(blank=True, help_text='horizontal', null=True, upload_to='cliente')),
            ],
            options={
                'verbose_name_plural': '1. Clientes ',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, help_text='imagenes 500*900', null=True, upload_to='media')),
            ],
            options={
                'verbose_name_plural': '2. Slider',
            },
        ),
        migrations.CreateModel(
            name='Vorti_Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=False)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='imagenes 50*50', null=True, upload_to='promo')),
                ('enlace', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '9. Promo Vortice',
            },
        ),
        migrations.CreateModel(
            name='Vortice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon_amarillo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('favicon_negro', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_horizontal', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='favicon')),
                ('logo_amarillo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_negro', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('representante', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('celular2', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('nosotros', models.TextField(blank=True, max_length=500, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='vortice')),
                ('imagen_encabezado', models.ImageField(blank=True, help_text='imagenes 500*400', null=True, upload_to='vortice')),
                ('imagen_fondo', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='vortice')),
                ('imagen_suscri', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='vortice')),
                ('imagen_pie', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='vortice')),
                ('imagen_flot_iz_1', models.ImageField(blank=True, help_text='imagenes 50*50', null=True, upload_to='vortice')),
                ('imagen_flot_iz_2', models.ImageField(blank=True, help_text='imagenes 50*50', null=True, upload_to='vortice')),
                ('imagen_flot_de_1', models.ImageField(blank=True, help_text='imagenes 50*50', null=True, upload_to='vortice')),
                ('imagen_flot_de_2', models.ImageField(blank=True, help_text='imagenes 50*50', null=True, upload_to='vortice')),
                ('wallpaper', models.ImageField(blank=True, help_text='imagenes 500*400', null=True, upload_to='vortice')),
            ],
            options={
                'verbose_name_plural': '1. Vortice',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(default=0)),
                ('offer', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('stock', models.BooleanField(default=True)),
                ('activar_camisetas', models.BooleanField(default=False)),
                ('camiseta_cuello_o', models.BooleanField(default=False)),
                ('camiseta_cuello_v_hombre_nene', models.BooleanField(default=False)),
                ('camiseta_cuello_v_mujer_nena', models.BooleanField(default=False)),
                ('camiseta_talla_hombre', models.BooleanField(default=False)),
                ('camiseta_talla_mujer', models.BooleanField(default=False)),
                ('camiseta_talla_nene', models.BooleanField(default=False)),
                ('camiseta_talla_nena', models.BooleanField(default=False)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('imagen_2', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('imagen_3', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('imagen_4', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('youtube', models.FileField(blank=True, null=True, upload_to='producto')),
                ('T_unica', models.BooleanField(default=False)),
                ('T_24', models.BooleanField(default=False)),
                ('T_26', models.BooleanField(default=False)),
                ('T_28', models.BooleanField(default=False)),
                ('T_30', models.BooleanField(default=False)),
                ('T_32', models.BooleanField(default=False)),
                ('T_34', models.BooleanField(default=False)),
                ('T_36', models.BooleanField(default=False)),
                ('T_38', models.BooleanField(default=False)),
                ('T_40', models.BooleanField(default=False)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=999)),
                ('precio_oferta', models.DecimalField(blank=True, decimal_places=2, max_digits=999, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('wallpapers', models.ImageField(blank=True, help_text='imagenes 500*400', null=True, upload_to='producto')),
                ('galeria_producto_1', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('galeria_producto_2', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('galeria_producto_3', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('galeria_producto_4', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('galeria_producto_5', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('galeria_producto_6', models.ImageField(blank=True, help_text='360x360', null=True, upload_to='producto')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('articulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.articulo')),
                ('prenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.prenda')),
            ],
            options={
                'verbose_name_plural': '1. Producto ',
            },
        ),
        migrations.AddField(
            model_name='coleccion',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vortice.seccion_cliente'),
        ),
        migrations.CreateModel(
            name='Camiseta_cuello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.seccion_cliente')),
            ],
            options={
                'verbose_name_plural': '6. Camiseta Cuello',
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='seccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.seccion_cliente'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vortice.imag_prenda_articulo'),
        ),
    ]