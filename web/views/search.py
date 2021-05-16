import requests
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import render, redirect
from django.utils.encoding import escape_uri_path

from script.create_folder import addImgToAlbum
from utils.Crawler import photo
from web import models


def search(request):
    # print(request.POST['question'])
    print(request.POST)
    # print(request.tracer.user.id)
    if not request.POST['question']:
        return render(request, 'index.html')
    models.UserHistory.objects.create(username=request.tracer.user.username,mobile_phone=request.tracer.user.mobile_phone,search=request.POST['question'])
    resultList = photo.getImgList(target=request.POST['question'], pn="1", userid=request.tracer.user.id)
    return render(request, 'search.html', {'img_list': resultList[2], 'num': resultList[0], 'str': resultList[1],
                                           'question': request.POST['question']})


# return render(request, 'project_list.html', {'form': form, 'project_dict': project_dict})

def download(request):
    print(request.POST)
    if request.POST['download']:
        res = requests.get(request.POST['imgsrc'])

        # 文件分块处理(适用于大文件)
        data = res.content

        # 设置content_type=application/octet-stream 用于提示下载框
        response = HttpResponse(data, content_type="application/octet-stream")

        response['Content-Disposition'] = "attachment; filename={}".format(
            escape_uri_path(request.POST['question'])) + ".png"
        return response

    return render(request, 'search.html')


# def download(request, url, question):
#     res = request.get(url)
#     data = res.content
#     response = HttpResponse(data)
#     response['Content-Disposition'] = "attachment; filename={}".format(question)
#     return response

def addpng(request):
    print(request.POST)
    addImgToAlbum(user_id=request.tracer.user.id, project=request.POST['project_name'],
                  filename=request.POST['imgname'], url=request.POST['imgurl'])
    return render(request, 'index.html', {'question': request.POST['imgname']})
