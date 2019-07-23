from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=20,verbose_name='轮播图标题')
    href = models.CharField(max_length=155,verbose_name="广告链接")
    src = models.ImageField(upload_to='imgs/banner/',verbose_name='图片')
    position = models.IntegerField(verbose_name='顺序')

    class Meta:
        db_table = 'banners'
        verbose_name_plural = verbose_name = '轮播图'

    def __str__(self):
        return self.title

class NewsType(models.Model):
    type_name = models.CharField(max_length=30,null=False,verbose_name="新闻类别")
    position = models.IntegerField(verbose_name="顺序")
    class Meta:
        db_table = "newstype"
        verbose_name_plural=verbose_name = "新闻类型"
    def __str__(self):
        return self.type_name

class News(models.Model):
    title  = models.CharField(max_length=150,null=False,verbose_name="新闻标题")
    href   = models.CharField(max_length=155,null=False,verbose_name="新闻链接")
    type   = models.ForeignKey(NewsType,on_delete=models.DO_NOTHING,max_length=130,verbose_name="新闻类型")
    origin = models.CharField(max_length=30,null=False,verbose_name="新闻来源")
    descrip= models.TextField(null=True,verbose_name="新闻简介")
    time = models.CharField(max_length=60,null=True,verbose_name="发布时间")
    picture = models.ImageField(upload_to="news/%Y/%m/%d",verbose_name="新闻配图")

    class   Meta:
        db_table = 'news'
        verbose_name_plural = verbose_name ='新闻'
    def __str__(self):
        return self.title



class CompanyModel(models.Model):
    big_title = models.CharField(max_length=30,null=False,verbose_name="大标题")
    little_title = models.CharField(max_length=30,null=False,verbose_name="小标题")
    content   = models.TextField(verbose_name="内容")
    uptime = models.DateTimeField(auto_now_add=True,verbose_name="更新时间")
    image  = models.ImageField(upload_to="company/%Y/%m/%d",null=True,verbose_name="配图")
    position = models.IntegerField(default=1,verbose_name='顺序')
    class Meta:
        db_table = "company"
        verbose_name_plural= verbose_name = "公司介绍"
    def __str__(self):
        return self.big_title

class Honor(models.Model):
    title = models.CharField(max_length=30,null=False,verbose_name="获奖名称")
    pic  = models.ImageField(upload_to= "honor/%Y/%m/%d",null=False,verbose_name="获奖照片")
    desc = models.CharField(max_length=155,null=True,verbose_name="获奖介绍")
    time = models.DateTimeField(auto_now_add=True,verbose_name="获奖时间")
    class Meta:
        db_table = "honor"
        verbose_name_plural = verbose_name = "公司荣誉"
    def __str__(self):
        return self.title

class Action_type(models.Model):
    type_name = models.CharField(max_length=30,null=False,verbose_name="活动大标题")

    class Meta:
        db_table = "action_type"
        verbose_name_plural = verbose_name = "活动大标题"

    def __str__(self):
        return self.type_name


class Action(models.Model):

    name = models.CharField(max_length=30,null=False,verbose_name="活动名称")
    img  = models.ImageField(upload_to= "action/%Y/%m/%d",null=False,verbose_name="活动照片")
    desc = models.CharField(max_length=155, null=True, verbose_name="活动介绍")
    time = models.DateTimeField(auto_now_add=True, verbose_name="活动时间")
    action_type = models.ForeignKey(Action_type,on_delete=models.DO_NOTHING,max_length=30,verbose_name="公司活动")
    class Meta:
        db_table = "action"
        verbose_name_plural = verbose_name = "活动细节"

    def __str__(self):
        return self.name

