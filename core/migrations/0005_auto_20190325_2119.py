# Generated by Django 2.1.7 on 2019-03-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190312_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profiles', verbose_name='Imagen'),
        ),
    ]
