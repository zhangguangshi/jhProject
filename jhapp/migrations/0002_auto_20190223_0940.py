# Generated by Django 2.1.4 on 2019-02-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstype',
            name='position',
            field=models.IntegerField(default=0, verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='position',
            field=models.IntegerField(default=0, verbose_name='顺序'),
        ),
    ]
