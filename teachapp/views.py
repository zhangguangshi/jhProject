from django.shortcuts import render
from teachapp.models import *
# Create your views here.

# 农技服务页面信息
def teach(request):
    # 轮播图广告
    banners = Teach_banner.objects.all().order_by("position")
    # 专家信息
    experts = ExpertModel.objects.all().order_by("time")
    # 推荐视频，根据播放量
    pop_videos = VideoModel.objects.all().order_by("times")[:8]
    # 最新视频，根据跟新时间
    videos  = VideoModel.objects.all().order_by("uptime")[:8]
    pop_videos  = VideoModel.objects.all().order_by("-times")[:8]
    data={
        "banners":banners,
        "exerpts":experts,
        "videos":videos,
        "pop_videos":pop_videos
    }
    return render(request,'teach.html',data)

# 推荐专家详情页
def experts(request,expert_id):
    expert = ExpertModel.objects.filter(id=expert_id)[0]
    # expert_videos = ExpertModel.objects.filter(expert=expert_id)
    context = {
        "expert":expert,
        # "videos":expert_videos
    }
    return render(request,'teach_video/expert_detail.html',context)

# 从数据库中取出视频信息
def video_list(request,type_name):
    pop_video = VideoModel.objects.all().order_by("-times")
    new_video = VideoModel.objects.all().order_by("uptime")
    category = VideoCategory.objects.all().order_by("id")

    video_list = []
    videos = []
    for cate in category:
        types = VideoType.objects.filter(category=cate)
        video_list.append(types)
    type_id = 0
    if type_name.isnumeric()==False:
        if type_name=="recom":
            type_name = "recom"
        elif type_name=="tests":
            type_name = "tests"
        else:
            print("输入网址参数错误！")
    else:
        type_id = int(type_name)
        type = VideoType.objects.filter( id=type_id)[0]
        videos = VideoModel.objects.filter(video_type=type)
        print(videos)
    data={
        "pop_video":pop_video,
        "new_video":new_video,
        "category":category,
        "video_list":video_list,
        "type_name":type_name,
        "type_id":type_id,
        "videos":videos
    }

    return render(request,'teach_video/video_list.html',data)

# 视频详情页的视图函数，拼接页面路径，查找数据库内容，传入前端页面
def video_detail(request,video_id):

    video = VideoModel.objects.get(id=video_id)


    context = {
        "video":video
    }
    return  render(request,'teach_video/video_detail.html',context)


