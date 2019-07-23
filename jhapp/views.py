from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from jhapp.models import *
from cirapp.models import PurchProductsModel
from teachapp.models import VideoModel
# 导航模块的试图函数
def index(request):
    # 查找数据库数据，找出所有的轮播图数据
    banners = Banner.objects.all().order_by('position')
    # 在导航页放入最新的八条新闻
    news = News.objects.all().order_by("-time")[:8]
    # 根据更新时间推荐最新的技术服务视频
    videos= VideoModel.objects.all().order_by("uptime")[:4]
    # 推荐最受欢迎的一个video
    pop_video=VideoModel.objects.all().order_by('-times')[0]
    # 农产品收购信息
    purpro = PurchProductsModel.objects.all()[:2]
    data = {
        'banners': banners,
        'news':news,
        'pop_video':pop_video,
        'videos':videos,
        'purpro':purpro
    }

    return render(request,'index.html',data)

def news(request,type_id,page_num):
    # 查找新闻类型遍历列表
    types = NewsType.objects.all().order_by("position")
    # 根据时间的顺序将新闻放入前端
    news = News.objects.filter(type_id=type_id).order_by("-time")
    # 对新闻进行分页，设置每页八条
    paginator = Paginator(news,8)
    # 进行分页
    page = paginator.page(page_num)
    pages_num = int(page_num)
    page_max = paginator.page_range
    data = {
        'types':types,
        'news':news,
        'web_id':int(type_id),
        "page_num":pages_num,
        "page":page,
        "page_max":len(page_max)
    }
    return  render(request,'news.html',data)

# 金融模块视图函数
def finance(request):
    return render(request,'finance.html')

# 关于公司模块试图函数
def company(request):
    honor = Honor.objects.all()
    action_type = Action_type.objects.all()

    data = {
        "honors":honor,
        "types":action_type
    }

    return render(request,'company.html',data)

