# Generated by Django 3.1.2 on 2020-10-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20201020_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.IntegerField(verbose_name='celular'),
        ),
    ]
