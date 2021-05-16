from django.shortcuts import render
import os

from web import models


def dashboard(request, project_id):
    project_name = models.Project.objects.filter(id=project_id).values('name')[0]['name']
    path = '/Users/jamesccc/Downloads/django--master-2/web/static/media/' + str(request.tracer.user.id) + '/' + str(
        project_name)
    imagename = os.listdir(path)
    path = '/media/' + str(request.tracer.user.id) + '/' + str(project_name) + '/'
    filepath = []
    for item in imagename:
        filepath.append({'file': path + item, "name": item})
    print(filepath)
    return render(request, 'dashboard.html', {'filepath': filepath, 'project_name': project_name})

