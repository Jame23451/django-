from django.shortcuts import render


def dashboard(request, project_id):
    return render(request, 'dashboard.html')


def setting(request, project_id):
    return render(request, 'setting.html')


def file(request, project_id):
    return render(request, 'file.html')
