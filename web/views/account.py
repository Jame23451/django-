"""
用户账户相关功能:注册、短信、登录、注销
"""
from io import BytesIO
from django.db.models import Q
from utils.image_code import check_code
from django.shortcuts import render, HttpResponse, redirect
from web.forms.account import RegisterModelForm, SendSmsForm, LoginSMSForm, LoginForm
from django.http import JsonResponse
from web import models

"""注册"""


def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过，写入数据库(密码要是密文)
        instance = form.save()
        return JsonResponse({'status': True, 'data': '/login/'})
    return JsonResponse({'status': False, 'error': form.errors})


"""发送短信"""


def send_sms(request):
    form = SendSmsForm(request, data=request.GET)
    # 只是校验手机号：不能为空、格式是否正确
    if form.is_valid():
        # 发短信 写入redis
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


"""短信登录"""


def login_sms(request):
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request, 'login_sms.html', {'form': form})
    form = LoginSMSForm(request.POST)
    if form.is_valid():
        # 用户输入正确，登录成功
        mobile_phone = form.cleaned_data['mobile_phone']
        #  用户信息放入session
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        request.session['user_id'] = user_object.id
        request.session.set_expiry(60 * 60 * 24 * 24)  # 主动修改session的过期时间
        print(user_object.username, user_object.email)
        return JsonResponse({"status": True, 'data': "/index/"})
    return JsonResponse({"status": False, 'error': form.errors})


"""用户名密码登录"""


def login(request):
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        # (手机=username and pwd=pwd) or (邮箱=username and pwd=pwd)

        user_object = models.UserInfo.objects.filter(Q(email=username) | Q(mobile_phone=username)).filter(
            password=password).first()

        if user_object:
            # 用户名密码正确 用户登录成功
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 24)  # 主动修改session的过期时间

            return redirect('index')
        form.add_error('username', '用户名或密码错误')
    return render(request, 'login.html', {'form': form})


"""生产图片验证码"""


def image_code(request):
    image_object, code = check_code()

    request.session['image_code'] = code
    request.session.set_expiry(60)  # 主动修改session的过期时间

    stream = BytesIO()
    image_object.save(stream, 'png')

    return HttpResponse(stream.getvalue())
