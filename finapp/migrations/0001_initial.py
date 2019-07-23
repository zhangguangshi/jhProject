# Generated by Django 2.1.7 on 2019-05-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('sex', models.BooleanField(choices=[(1, '男'), (0, '女')], verbose_name='性别')),
                ('idnumber', models.CharField(max_length=18, verbose_name='身份证号')),
                ('tel', models.CharField(max_length=11, verbose_name='手机号码')),
                ('adress', models.CharField(max_length=50, verbose_name='地址')),
                ('area', models.CharField(max_length=10, verbose_name='种植亩数')),
                ('money', models.CharField(max_length=12, verbose_name='需求资金')),
            ],
            options={
                'verbose_name': '贷款申请表',
                'verbose_name_plural': '贷款申请表',
                'db_table': 'finance_form',
            },
        ),
    ]
