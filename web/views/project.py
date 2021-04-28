from django.shortcuts import render


def project_list(request):
    """收藏列表"""
    return render(request, 'project_list.html')
