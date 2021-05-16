#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from script import create_folder
from web.forms.project import ProjectModelForm
from web import models


# from utils.tencent.cos import create_bucket


def project_list(request):
    """ 项目列表 """
    if request.method == "GET":
        # GET请求查看项目列表
        project_dict = {'star': [], 'my': []}
        my_project_list = models.Project.objects.filter(creator=request.tracer.user)
        for row in my_project_list:
            if row.star:
                project_dict['star'].append({"value": row, 'type': 'my'})
            else:
                project_dict['my'].append(row)

        form = ProjectModelForm(request)
        return render(request, 'project_list.html', {'form': form, 'project_dict': project_dict})

    # POST，对话框的ajax添加项目。
    form = ProjectModelForm(request, data=request.POST)
    if form.is_valid():
        form.instance.creator = request.tracer.user
        form.save()
        create_folder.addAlbum(user_id=str(form.instance.creator_id), filename=form.instance.name)
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def project_star(request, project_id):
    """ 星标项目 """
    models.Project.objects.filter(id=project_id, creator=request.tracer.user).update(star=True)
    return redirect('project_list')


def project_unstar(request, project_id):
    """ 取消星标 """
    models.Project.objects.filter(id=project_id, creator=request.tracer.user).update(star=False)
    return redirect('project_list')

# def download(request):
#     print(request.POST)
#     if request.POST['download']:
#         res = requests.get(request.POST['imgsrc'])
#
#         # 文件分块处理(适用于大文件)
#         data = res.content
#
#         # 设置content_type=application/octet-stream 用于提示下载框
#         response = HttpResponse(data, content_type="application/octet-stream")
#
#         response['Content-Disposition'] = "attachment; filename={}".format(
#             escape_uri_path(request.POST['question'])) + ".png"
#         return response
#
#     return render(request, 'search.html')