# Generated by Django 2.1.7 on 2019-05-18 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='监控名')),
                ('number', models.IntegerField(verbose_name='监控编号')),
                ('href', models.CharField(max_length=155, verbose_name='接口')),
                ('img', models.ImageField(upload_to='JK/%Y/%m/%d', verbose_name='商品图片')),
                ('desc', models.CharField(max_length=60, verbose_name='描述')),
            ],
            options={
                'verbose_name': '监控',
                'verbose_name_plural': '监控',
                'db_table': 'monit',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('phone', models.CharField(default='', max_length=11, verbose_name='手机号')),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finapp.Finance_form', verbose_name='贷款申请表')),
                ('monit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.MonitModel', verbose_name='监控设备')),
            ],
            options={
                'verbose_name': '普通用户',
                'verbose_name_plural': '普通用户',
                'db_table': 'user',
            },
        ),
    ]
