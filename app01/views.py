from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return render(request, 'user_add.html')

def tpl(request):
    name = "赵诚智"
    roles = ['管理员', 'CEO', '保安']
    user_info = {'name': '张三', 'roles': '保安', 'salary': 10000}
    data_list = [
        {'name': '张三', 'roles': '保安', 'salary': 10000},
        {'name': '李四', 'roles': '总经理', 'salary': 20000},
        {'name': '王五', 'roles': '董事长', 'salary': 30000},
        {'name': '赵六', 'roles': '大厅经理', 'salary': 40000}
    ]

    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})

def news(request):
    return render(request, 'news.html')

def something(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    # return HttpResponse('返回内容')
    # return render(request,'something.html',{"item":'来了'})
    return redirect('https://www.baidu.com/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username == 'root' and password == 'root123':
            return redirect('https://www.baidu.com/')
        else:
            return render(request,'login.html',{'error':'用户名或密码错误'})

def orm(request):
    # models.Department.objects.create(title='销售部')
    # models.Department.objects.create(title='IT部')
    # models.Department.objects.create(title='运营部')
    # models.UserInfo.objects.create(name='张三', password='123', age=18)
    # models.UserInfo.objects.create(name='李四', password='456', age=19)
    # models.UserInfo.objects.create(name='王五', password='789', age=20)
    # models.UserInfo.objects.filter(id=3).delete()
    # models.Department.objects.all().delete()
    # data_list = models.UserInfo.objects.filter(id=1)
    # data_list = models.UserInfo.objects.filter(id=1).first()
    models.UserInfo.objects.all().update(password = '999')
    models.UserInfo.objects.filter(id=2).update(age=999)
    return HttpResponse('成功!')

def info_list(request):
    data_list = models.UserInfo.objects.all()
    return render(request,'info_list.html',{'data_list':data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request,'info_add.html')
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    models.UserInfo.objects.create(name=name,password=password,age=age)

    return redirect('http://127.0.0.1:8000/info/list/')

def info_delete(request):
    id = request.GET.get('nid')
    models.UserInfo.objects.filter(id=id).delete()
    return redirect('/info/list')