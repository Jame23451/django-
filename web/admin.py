from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(UserInfo)
admin.site.register(Project)
admin.site.register(UserHistory)
admin.site.register(order)