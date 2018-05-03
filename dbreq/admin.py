from django.contrib import admin

# Register your models here.
from dbreq import models
# 把models创建的表添加到admin后台中
admin.site.register(models.UserInfor)