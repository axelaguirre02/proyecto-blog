# Generated by Django 4.0.5 on 2022-08-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0002_alter_articulo_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='actualizado',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizado'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
    ]
