from django.db import models

# Create your models here.

class PurchaserModel(models.Model):
    name = models.CharField(max_length=30,verbose_name="采购商名")
    pic  = models.ImageField(upload_to="imgs/purchaser/",verbose_name='采购商logo')
    desc = models.TextField(verbose_name="公司介绍")

    class Meta:
        db_table = 'purchaser'
        verbose_name_plural = verbose_name = '采购商'
    def __str__(self):
        return self.name

class PurchProductsModel(models.Model):
    purchaser = models.ForeignKey(PurchaserModel,on_delete=models.CASCADE,verbose_name='采购商')
    title    = models.CharField(max_length=30,verbose_name='采购名称')
    pic      = models.ImageField(upload_to="imgs/purchs/",verbose_name="采购产品图")
    desc     = models.CharField(max_length=255,verbose_name="采购简介")
    count    = models.IntegerField(default='98',verbose_name='采购数量')
    class Meta:
        db_table = 'purch_products'
        verbose_name_plural = verbose_name = "采购产品"
    def __str__(self):
        return self.title






