# Generated by Django 4.0.5 on 2022-08-16 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articulos', '0003_alter_articulo_actualizado_alter_articulo_creado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='usuario',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario:'),
        ),
    ]