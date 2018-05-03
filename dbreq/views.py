from django.shortcuts import render
from dbreq import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
# 增加操作
def userInfor(req):
    if req.method == "POST":
        u = req.POST.get("username", None)
        s = req.POST.get("sex", None)
        e = req.POST.get("email", None)
        info={"username":u,"sex":s,"email":e}
        # 增加数据
        models.UserInfor.objects.create(**info)
        info_list=models.UserInfor.objects.all()
        return render(req, "userInfor.html", {"info_list":info_list})
    return render(req, "userInfor.html")

def show(req):
    info_list=models.UserInfor.objects.all() # 取出该表所有数据

    return  render(req,'show.html',{'info_list':info_list})


# 删除操作
@csrf_exempt
def delData(req):
    # 删除数据
    info_list = models.UserInfor.objects.filter(username='哈哈哈')
    return render(req, "show.html", {"info_list": info_list})

# 修改操作
@csrf_exempt
def updateData(req):
    models.UserInfor.objects.filter(username='哈哈哈').update(sex='女',email='yixiugai@163.com')
    info_list = models.UserInfor.objects.all()
    return render(req,"show.html",{"info_list":info_list})