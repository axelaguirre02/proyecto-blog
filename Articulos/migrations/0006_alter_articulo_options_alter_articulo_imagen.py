# Generated by Django 4.0.5 on 2022-08-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0005_alter_articulo_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'ordering': ['-creado'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='null', upload_to='articulos', verbose_name='Imagen:'),
        ),
    ]
