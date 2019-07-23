from django.shortcuts import render
from goodsapp.models import MerchModel,CategoryModel,GoodsModel,PackageModel
# Create your views here.

def goods(request):
    merch_pic1 = MerchModel.objects.first()
    merch_pics = MerchModel.objects.all().order_by("position")[1:]
    packages = PackageModel.objects.all().order_by("-position")[:4]
    goods = GoodsModel.objects.all().order_by("popular")[:8]

    context = {
        "merch_pic1":merch_pic1,
        "merch_pics":merch_pics,
        "goods_list":goods,
        "packages":packages
    }

    return render(request,'goods.html',context)

def goods_list(request,category_id):
    type = CategoryModel.objects.get(id=category_id)
    category_list = CategoryModel.objects.all()
    query_set = GoodsModel.objects.filter(category_id=category_id).order_by("-popular")
    populars = GoodsModel.objects.all().order_by("-popular")
    # 对商品进行分页
    data={
        "type":type,
        "categorys":category_list,
        "goods":query_set,
        "populars":populars,
        "category_id":category_id
    }

    return render(request,'goods_list/goods_list.html',data)

def goods_detail(reqesut,goods_id,sort):
    goods = GoodsModel.objects.filter(id=goods_id)[0]
    news = GoodsModel.objects.all().order_by("-popular")[:3]
    category_list = CategoryModel.objects.all()
    info=[]
    if sort=="detail":
        info = goods.desc
    elif sort=="desc":
        info = goods.goods_origin.origin_desc
    else:
        print("访问错误！")

    data = {
        "goods":goods,
        "news":news,
        "goods_id":goods_id,
        "category_list":category_list,
        "info":info,
        "sort":sort
    }

    return render(reqesut,'goods_list/goods_detail.html',data)

