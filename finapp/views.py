from django.shortcuts import render

# Create your views here.
from finapp.models import Finance_form

def finance_con(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        sex  = request.POST.get('sex')
        idnumber = request.POST.get('idNumber')
        tel  = request.POST.get('tel')
        adress=request.POST.get('adress')
        area = request.POST.get('area')
        money = request.POST.get('monney')

        form = Finance_form()
        form.name = name
        form.sex = int(sex)
        form.idnumber=idnumber
        form.tel = tel
        form.adress=adress
        form.area = area
        form.money = money

        form.save()
        return render(request,'finance_con.html')
    else:
        return render(request, 'finance_con.html')



