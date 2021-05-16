import datetime
import json

from django.shortcuts import render, redirect

from web import models


def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


def price(request):
    policy_list = models.PricePolicy.objects.filter(category=2)
    return render(request, 'price.html', {'policy_list': policy_list})


def pay(request):
    return render(request, 'pay.html')


def complite(request):
    models.UserInfo.objects.filter(id=request.tracer.user.id).update(isvip=True)
    models.order.objects.create(username=request.tracer.user.username,
                                      mobile_phone=request.tracer.user.mobile_phone)
    return redirect('index')
