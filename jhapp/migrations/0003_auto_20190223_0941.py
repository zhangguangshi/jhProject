# Generated by Django 2.1.4 on 2019-02-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhapp', '0002_auto_20190223_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='position',
            field=models.IntegerField(verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='newstype',
            name='position',
            field=models.IntegerField(verbose_name='顺序'),
        ),
    ]
