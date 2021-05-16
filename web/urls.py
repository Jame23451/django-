from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from djangoProject import settings
from web.views import account, home, project, manage, search

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^login/$', account.login, name='login'),
    # url(r'^loginAdmin/$', account.loginAdmin, name='loginAdmin'),
    # url(r'^admin/$', admin.site.root),
    url(r'^image/code/$', account.image_code, name='image_code'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),
    url(r'^logout/$', account.logout, name='logout'),
    url(r'^index/$', home.index, name='index'),
    url(r'^price/$', home.price, name="price"),
    url(r'^price/pay/$', home.pay, name='pay'),
    url(r'^price/complite/$', home.complite, name='complite'),
    # 搜索页面
    url(r'^search/$', search.search, name='search'),
    url(r'^search/download/$', search.download, name='download'),
    url(r'^search/addpng/$', search.addpng, name='addpng'),

    # 收藏夹
    url(r'^project/list/$', project.project_list, name='project_list'),
    url(r'^project/star/(?P<project_id>\d+)/$', project.project_star, name='project_star'),
    url(r'^project/unstar/(?P<project_id>\d+)/$', project.project_unstar, name='project_unstar'),

    url(r'^manage/(?P<project_id>\d+)/', include([
        url(r'^dashboard/$', manage.dashboard, name='dashboard'),
    ], None)),
]
