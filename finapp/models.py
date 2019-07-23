from django.db import models

# Create your models here.


class Finance_form(models.Model):

    name     = models.CharField(max_length=20,null=False,verbose_name="用户名")
    sex      = models.BooleanField(choices=((1,"男"),(0,"女")),null=False,verbose_name='性别')
    idnumber = models.CharField(max_length=18,null=False, verbose_name='身份证号')
    tel      = models.CharField(max_length=11,null=False, verbose_name='手机号码')
    adress   = models.CharField(max_length=50,null=False, verbose_name="地址")
    area     = models.CharField(max_length=10,null=False,verbose_name='种植亩数')
    money   = models.CharField(max_length=12,null=False,verbose_name='需求资金')

    class Meta:
        db_table = "finance_form"
        verbose_name_plural = verbose_name = "贷款申请表"

    def __str__(self):
        return self.name