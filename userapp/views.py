from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password,check_password
import random
import urllib
from urllib.parse import urlencode
import http
from http.client import HTTPConnection
from userapp.util import login_required
from userapp.models import UserModel,MonitModel,Finance_form

# Create your views here.

def register(request):
    """注册"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('tel', '')
        code = request.POST.get('code', '')
        message_code = request.session.get('message_code')
        print(username, password, phone, code, message_code)

        if code == message_code:
            # 新建用户
            user = UserModel()
            user.username = username
            user.password = make_password(password)
            user.phone = phone
            user.save()
            return redirect('user:login')
        else:
            #验证码错误
            return render(request, 'user/register.html', {'is_code': 0})
    return  render(request, 'user/register.html', {'is_code': 1})

def login(request):
    """登录"""
    if request.method == 'POST':
        phone = request.POST.get('username', '')
        password = request.POST.get('pwd', '')
        # print(phone,'+' , password)

        # 根据手机号来查询用户对象
        user = UserModel.objects.filter(phone=phone)

        # 判断如果没有查到说明手机号错误，如果查到判断密码是否正确
        # 密码错误，返回登录页面，并且提示密码错误
        if user:
            user = user[0]
            # print(user.password)
            # 检查密码是否正确
            is_password = check_password(password, user.password)
            # pwd = user.password
            # if password != pwd:
            if not is_password:
                # 密码错误
                return render(request, 'user/login.html', {"is_password": 1, 'is_user': 0})
            else:
                # 密码正确
                # 把用户id和username放入session中
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username

                # 记住用户名并且设置cookies
                next_url = request.COOKIES.get('next_url', reverse('jh:index'))
                return redirect(next_url)
        else:
            #手机号不正确
            return render(request, 'user/login.html', {'is_user': 1, 'is_password': 0})
    return render(request, 'user/login.html', {'is_password': 0, 'is_user': 0})

# 修改密码
def update_pwd(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        phone = request.POST.get('tel', '')
        code = request.POST.get('code', '')
        message_code = request.session.get('message_code')
        print(password, phone, code, message_code)
        #查找手机号
        user = UserModel.objects.filter(phone=phone)
        #判断验证码
        if code == message_code:
            user = user[0]
            #更新密码
            user.password = make_password(password)
            user.save()
        else:
            #验证码错误
            return render(request, 'user/update_pwd.html', {'is_code': 0})
        return redirect('user:login')
    return  render(request, 'user/update_pwd.html', {'is_code': 1})

# 退出登录
def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect(reverse('jh:index'))

# 短信验证码
# 请求的路径
host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
# 用户名是登录ihuyi.com账号名（例如：cf_demo123）
account = "C44358674"
# 密码 查看密码请登录用户中心-&gt;验证码、通知短信-&gt;帐户及签名设置-&gt;APIKEY
password = "6f835269b467197daf6bbf6635253935"

def send_message(request):
    """发送信息的视图函数"""
    # 获取ajax的get方法发送过来的手机号码
    mobile = request.GET.get('mobile')
    print(mobile)
    # 通过手机去查找用户是否已经注册
    user = UserModel.objects.filter(phone=mobile)
    if user:
        msg = '手机号已注册'
        return HttpResponse(msg)
    else:
        #发送验证码
        # 定义一个字符串,存储生成的6位数验证码
        message_code = ''
        for i in range(6):
            i = random.randint(0, 9)
            message_code += str(i)
        # 拼接成发出的短信
        text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
        # 把请求参数编码
        params = urllib.parse.urlencode(
            {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
        # 请求头
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        # 通过全局的host去连接服务器
        conn = http.client.HTTPConnection(host, port=80, timeout=30)
        # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
        conn.request("POST", sms_send_uri, params, headers)
        # 得到服务器的响应
        response = conn.getresponse()
        # 获取响应的数据
        response_str = response.read()
        # 关闭连接
        conn.close()
        # 把验证码放进session中
        request.session['message_code'] = message_code
        # print(eval(response_str.decode()))
        # 使用eval把字符串转为json数据返回
        # return JsonResponse(eval(response_str.decode()))
        msg = '提交成功'
        return HttpResponse(msg)

def send_update_message(request):
    # 获取ajax的get方法发送过来的手机号码
    mobile = request.GET.get('mobile')
    print(mobile)
    # 通过手机去查找用户是否已经注册
    user = UserModel.objects.filter(phone=mobile)
    if user:
        # 已注册就发送验证码
        # 定义一个字符串,存储生成的6位数验证码
        message_code = ''
        for i in range(6):
            i = random.randint(0, 9)
            message_code += str(i)
        # 拼接成发出的短信
        text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
        # 把请求参数编码
        params = urllib.parse.urlencode(
            {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
        # 请求头
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        # 通过全局的host去连接服务器
        conn = http.client.HTTPConnection(host, port=80, timeout=30)
        # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
        conn.request("POST", sms_send_uri, params, headers)
        # 得到服务器的响应
        response = conn.getresponse()
        # 获取响应的数据
        response_str = response.read()
        # 关闭连接
        conn.close()
        # 把验证码放进session中
        request.session['message_code'] = message_code
        # print(eval(response_str.decode()))
        # 使用eval把字符串转为json数据返回
        # return JsonResponse(eval(response_str.decode()))
        msg = '提交成功'
        return HttpResponse(msg)
    else:
        msg = '手机号未注册'
        return HttpResponse(msg)

@login_required
def user_center(request):
    user_id = request.session["user_id"]
    user  = UserModel.objects.filter(id=user_id)[0]
    monit = MonitModel.objects.all()
    data = {
        'user':user,
        'monits':monit,
        'name':user.username,
        "phone":user.phone
    }
    return render(request,'user/user_center.html',data)


@login_required
def monit_detail(request,number):
    monit_detail = MonitModel.objects.filter(number=number)[0]
    monits =  MonitModel.objects.all()
    user = UserModel.objects.all()[0]
    data={
        "monit":monit_detail,
        "user":user,
        "others":monits
    }
    return render(request,'user/user_video.html',data)


