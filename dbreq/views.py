from django.shortcuts import render
from dbreq import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def userInfor(req):
    if req.method == "POST":
        u = req.POST.get("username", None)
        s = req.POST.get("sex", None)
        e = req.POST.get("email", None)
        info={"username":u,"sex":s,"email":e}
        models.UserInfor.objects.create(**info)
        info_list=models.UserInfor.objects.all()
        return render(req, "userInfor.html", {"info_list":info_list})
    return render(req, "userInfor.html")


