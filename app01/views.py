from django.shortcuts import render, HttpResponse
import random

from django_redis import get_redis_connection

from utils.Tencent.SMS import send_sms_single
from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings


def send_sms(request):
    """发送短信"""
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse('模板不存在')
    code = random.randrange(1000, 9999)
    res = send_sms_single('17775719496', template_id, [code, ])
    print(res)
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res)


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "请输入密码"}))
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "请重复输入密码"}))
    code = forms.CharField(label='验证码', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "请输入验证码"}))

    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)


def register(request):
    form = RegisterModelForm()
    return render(request, 'app01/register.html', {'form': form})


def index(request):
    # 去连接池中获取一个连接
    conn = get_redis_connection("default")
    conn.set('nickname', "武沛齐", ex=10)
    value = conn.get('nickname')
    print(value)
    return HttpResponse("OK")
