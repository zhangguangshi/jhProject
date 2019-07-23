from django.db import models
from finapp.models import Finance_form
# Create your models here.

class MonitModel(models.Model):
    title = models.CharField(max_length=20,null=False,verbose_name="监控名")
    number = models.IntegerField(null=False,verbose_name="监控编号")
    href  = models.CharField(max_length=155,null=False,verbose_name="接口")
    img   = models.ImageField(upload_to="JK/%Y/%m/%d", verbose_name="商品图片")
    desc   = models.CharField(max_length=60,null=False,verbose_name="描述")
    class Meta:
        verbose_name_plural = verbose_name = '监控'
        db_table = 'monit'

    def __str__(self):
        return self.title

class UserModel(models.Model):
    """用户数据模型"""
    # 用户名(手机号)
    username = models.CharField(max_length=50, null=False, verbose_name="用户名")
    # 密码
    password = models.CharField(max_length=256, null=False, verbose_name='密码')
    # 手机号
    phone = models.CharField(max_length=11, null=False, verbose_name='手机号', default="")
    # 申请表
    form  = models.ForeignKey(Finance_form,on_delete=models.CASCADE,null=True,verbose_name="贷款申请表")
    # 监控
    monit = models.ForeignKey(MonitModel,on_delete=models.CASCADE,null=True,verbose_name="监控设备")

    # 地址
    # address = models.CharField(max_length=200, null=True, verbose_name='地址', blank=True)
    # 电子邮箱
    # email = models.EmailField(verbose_name='电子邮箱', null=True, blank=True)
    class Meta:
        verbose_name_plural = verbose_name = '普通用户'
        db_table = 'user'

    def __str__(self):
        return self.username
