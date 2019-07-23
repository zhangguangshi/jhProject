from django.db import models

# Create your models here.

class MerchModel(models.Model):
    name = models.CharField(max_length=20,verbose_name="商家名字")
    href = models.CharField(max_length=155,verbose_name="商家广告链接")
    src = models.ImageField(upload_to='imgs/goods_list/',verbose_name="图片")
    position = models.IntegerField(verbose_name="顺序")

    class Meta:
        db_table = 'merch'
        verbose_name_plural = verbose_name = "商家广告"
    def __str__(self):
        return self.name

class PackageModel(models.Model):
    name = models.CharField(max_length=20,verbose_name="精选套餐名字")
    href = models.CharField(max_length=155,verbose_name="套餐链接")
    src = models.ImageField(upload_to='imgs/goods_list/',verbose_name="广告图片")
    position = models.IntegerField(verbose_name="顺序")

    class Meta:
        db_table = 'package'
        verbose_name_plural = verbose_name = "套餐广告"
    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    """商品的分类"""
    category_name = models.CharField(max_length=30,null=False,verbose_name="商品类名")

    class Meta:
        db_table = "category"
        verbose_name_plural = verbose_name = "产品分类"
    def __str__(self):
        return self.category_name

class GoodsOrigin(models.Model):
    """商品来源"""
    origin_name = models.CharField(max_length=30,null=False,verbose_name="商品来源")
    origin_pic = models.ImageField(upload_to="goods_origin/",verbose_name="商家logo")
    origin_desc = models.TextField(default="暂无",verbose_name="商家介绍")
    class Meta:
        db_table = "goods_origin"
        verbose_name_plural=verbose_name = "商品源"
    def __str__(self):
        return self.origin_name


class GoodsModel(models.Model):
    """商品模型"""
    goods_name = models.CharField(max_length=50, null=False, verbose_name="商品名称")
    abstract = models.CharField(max_length=80, null=False, verbose_name="商品简介")
    # max_digits 总共限制几位，decimal_places 小数点后的第几位
    price = models.DecimalField(default=0, max_digits=11, decimal_places=2, verbose_name="商品价格")
    unit = models.CharField(max_length=30, null=False, verbose_name="商品的售卖单位")
    stock = models.IntegerField(default=0, verbose_name="商品库存")
    desc = models.TextField(null=True, verbose_name="详细介绍")
    pic = models.ImageField(upload_to="goods_list/%Y/%m/%d", verbose_name="商品图片")
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING, verbose_name="商品的分类")
    popular = models.IntegerField(default=0, verbose_name="人气指数")
    goods_origin = models.ForeignKey(GoodsOrigin,on_delete=models.DO_NOTHING,verbose_name="商品源")
    class Meta:
        db_table= "goods"
        verbose_name_plural = verbose_name = "商品"
    def __str__(self):
        return self.goods_name

