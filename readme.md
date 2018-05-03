# 提交数据至数据库，并在后台管理操作
```
# 首先创建django项目，其项目目录如下：
exa
  ---dbreq
    ---migrations
      ---__init__.py
    ---admin.py
	---apps.pyy
    ---models.py
    ---tests.py
    ---views.py
  ---exa
    ---__init__.py
    ---settings.py
    ---urls.py
    ---wsgi.py
  ---templates
    ---userInfor.html
  ---db.sqlites
  ---manage.py
```

>/templates/userInfor.html

```html
<h1>创建个人信息</h1>
<form action="/userInfor/" method="post">
    {% csrf_token %}
    <p>姓名<input type="text" name="username"></p>
    <p>性别<input type="text" name="sex"></p>
    <p>邮箱<input type="text" name="email"></p>
    <p><input type="submit" value="submit"></p>
</form>
<hr>
<h1>信息展示</h1>
<table border="1">
    <tr>
        <td>姓名</td>
        <td>性别</td>
        <td>邮箱</td>
    </tr>
    {% for i in info_list %}
        <tr>
            <td>{{ i.username }}</td>
            <td>{{ i.sex }}</td>
            <td>{{ i.email }}</td>
        </tr>
    {% endfor %}
</table>
```
>/exa/urls.py

```python
# 添加以下代码
path('userInfor/', views.userInfor),
```

>/dbreq/views.py
```python
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

```
>models.py

```
# 创建数据库
from django.db import models

# Create your models here.
class UserInfor(models.Model):
    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)

```

>以上.py文件写完后，生成表
```python
# 生成相应的表:
python manage.py makemigrations
python manage.py migrate
```
>为项目后台数据库设置账户
```python
python manage.py createsuperuser
```

>此时运行python manage.py runserver 8088，然后http://localhost:8000/admin 登录账户后，会发现无表，此时需要对admin.py进行修改
```
# admin.py
from django.contrib import admin

# Register your models here.
from dbreq import models
# 把models创建的表添加到admin后台中
admin.site.register(models.UserInfor)
```
此时后台如下界面：
![](http://p20tr36iw.bkt.clouddn.com/sqli3.png)
>此时进行增加数据操作

```python
http://127.0.0.1:8000/userInfor/
```
页面创建表，后台实时更新成功，如图！

<img src="http://p20tr36iw.bkt.clouddn.com/sqli1.png" style="float:left"/>
<img src="http://p20tr36iw.bkt.clouddn.com/sqli2.png" style="float:left"/>
