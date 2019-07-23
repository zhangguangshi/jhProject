from django.db import models

# Create your models here.

#视频界面主页轮播图
class Teach_banner(models.Model):
    title = models.CharField(max_length=20,verbose_name='轮播图标题')
    href = models.CharField(max_length=155,verbose_name="广告链接")
    src = models.ImageField(upload_to='imgs/banner/',verbose_name='图片')
    position = models.IntegerField(verbose_name='顺序')

    class Meta:
        db_table = 'teach_banners'
        verbose_name_plural = verbose_name = '轮播图'

    def __str__(self):
        return self.title


class ExpertModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='专家姓名',default="未知")
    sex  = models.BooleanField(choices=((1,"男"),(0,"女")),verbose_name="性别")
    age  = models.IntegerField(verbose_name="年龄")
    post = models.CharField(max_length=20,verbose_name='职称',null=True)
    professional = models.CharField(max_length=30,verbose_name='专业领域',null = False )
    time = models.CharField(max_length=20,verbose_name='从业时长',null=True)
    pic  = models.ImageField(upload_to="imgs/expert/",verbose_name='头像',)
    desc = models.TextField(verbose_name="个人简介")

    class Meta:
        db_table = "expert"
        verbose_name_plural = verbose_name = "专家"

    def __str__(self):
        return self.name

class VideoCategory(models.Model):
    category = models.CharField(max_length=30,verbose_name='视频类别')
    class Meta:
        db_table = "video_category"
        verbose_name_plural = verbose_name = "视频类别"

    def __str__(self):
        return self.category

class VideoType(models.Model):
    type = models.CharField(max_length=30,verbose_name='视频类型')
    category = models.ForeignKey(VideoCategory,on_delete=models.DO_NOTHING,verbose_name='视频大类别',default=1)
    class Meta:
        db_table = "video_type"
        verbose_name_plural = verbose_name = "视频类型"

    def __str__(self):
        return self.type

class VideoModel(models.Model):
    title = models.CharField(max_length=20,verbose_name="课程名称")
    href  = models.CharField(max_length=155,verbose_name="视频链接")
    img   = models.ImageField(upload_to='imgs/video/',verbose_name='视频图片')
    desc   = models.CharField(max_length=255,verbose_name='课程介绍')
    expert = models.ManyToManyField(ExpertModel,verbose_name='课程讲师')
    video_type  = models.ManyToManyField(VideoType,verbose_name="视频类型")
    video_category=models.ManyToManyField(VideoCategory,verbose_name="视频大类别",default=1)
    uptime = models.DateTimeField(auto_now_add=True,verbose_name="更新时间")
    times = models.IntegerField(default=0,verbose_name="视频播放量")

    class Meta:
        db_table = "video"
        verbose_name_plural = verbose_name = "课程视频"

    def __str__(self):
        return self.title





