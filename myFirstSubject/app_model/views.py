from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AppModel
from .forms import Register,Login
from .models import MyUser
import datetime


# Create your views here.
def app_index(request,**kwargs):
    # appData = AppModel(name='cla',age=123)
    # appData.save()
    # AppModel.objects.create(name='java',age=100)
    AppModel.objects.get_or_create(name='python',age=80)
    return render(request,'index.html',context={'name':'保存成功python'})

def select_index(request,**kwargs):
    # getAll = AppModel.objects.all()
    # getAll = AppModel.objects.get(id='1')
    getAll = AppModel.objects.filter()
    print(getAll)
    return render(request,'app_index.html',context={'name':'查询成功'})

def update_index(request,**kwargs):
    # upData = AppModel.objects.get(id=2)
    # upData.name = 'javascript'
    # upData.age = 60
    # upData.save()
    AppModel.objects.filter(id=1).update(name='c',age=120)
    # AppModel.objects.get(id=1).update(name='c++',age=140) 更新只能改变querySet 对象
    print(AppModel.objects.filter())
    return HttpResponse('更新成功·')

def deteDate_index(request,**kwargs):
    # AppModel.objects.get(id=1).delete()
    AppModel.objects.filter(id=1).delete()
    return HttpResponse('删除数据')


def log(request,**kwargs):
    if request.method == 'GET':
        return render(request,'add_session.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.getlist('password')
        if password[0] != password[1]:
            print(password[0],password[1])
            return HttpResponse('两次密码不一致')
        else:
            request.session['username'] = username
            # request.session.set_expiry(200)
            return HttpResponse('登陆成功')

def get_session(request,**kwargs):
    username = request.session.get('username','none')
    return render(request,'get_session.html',context={'username':username})

def logout(request,**kwargs):
    request.session.flush()
    return redirect('/appModel/add_session')

def register(request,**kwargs):
    if request.method == 'GET' :
        form = Register()
        return render(request,'register.html',context={'form':form})
    elif request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            re_password = form.cleaned_data.get('re_password')
            email = form.cleaned_data.get('email')
            if password == re_password:
                MyUser.objects.create(username=username,password=password,email=email)
                return HttpResponse('注册成功')
            else:
                return HttpResponse('注册失败')
        else:
            form = Register()
            return render(request, 'register.html', context={'form': form})

def login(request,**kwargs):
    if request.method == 'GET':
        return  render(request,'login.html')
    elif request.method == 'POST':
        login = Login(request.POST)
        if login.is_valid():
            username = login.cleaned_data.get('username')
            password = login.cleaned_data.get('password')
            myuser = MyUser.objects.filter(username=username,password=password)
            if myuser:
                request.session['username'] = username;
                request.session.set_expiry(datetime.timedelta(2019, 1, 12, 14, 26, 10, 3257, tzinfo=None))
                return HttpResponse('登陆成功')
            else:
                return HttpResponse('登陆失败')
        else:
            return render(request, 'login.html')

