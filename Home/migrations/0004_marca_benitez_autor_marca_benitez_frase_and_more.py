# Generated by Django 4.0.6 on 2022-07-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_marca_benitez_estudio_marca_benitez_calle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca_benitez',
            name='autor',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='marca_benitez',
            name='frase',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='marca_benitez',
            name='nosotros',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
    ]
