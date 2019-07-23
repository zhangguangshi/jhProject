from django.shortcuts import render
from cirapp.models import PurchProductsModel,PurchaserModel
# Create your views here.

def cir(request):
    purchaser = PurchaserModel.objects.all()
    purpro    = PurchProductsModel.objects.all()[:2]

    context = {
        "purchaser":purchaser,
        "purpro":purpro
    }
    return render(request,'cir.html',context=context)

def cir_detail(request,pur_id):
    companys = PurchaserModel.objects.all()
    content = PurchaserModel.objects.filter(id=pur_id)[0]
    context = {
        "companys":companys,
        "pur_id":pur_id,
        "content":content
    }
    return render(request,"cirs/company_detail.html",context)

