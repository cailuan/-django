from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Register
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def index(request):
    return render(request,'app_suth/index.html')

def register(request):
    if request.method == 'GET':
        return render(request,'app_suth/register.html')
    elif request.method == 'POST':
        form = Register(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            re_password = form.cleaned_data.get('re_password')
            email = form.cleaned_data.get('email')
            print(password, re_password)
            if password == re_password:
                User.objects.create_user(username=username,password=password,email=email)
                return HttpResponse('创建成功')
            else:
                return HttpResponse('创建失败')
        return HttpResponse('注册失败')

def login_suth(request):
    if request.method == 'GET':
        return render(request,'app_suth/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            myuser = request.user
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return HttpResponse(myuser)
        else:
            HttpResponse('不存在用户')


def logout_suth(request):
    print(request.user.is_authenticated) //True
    logout(request)
    print(request.user)
    return HttpResponse('登出')

@permission_required('app_model.add_appmodel')
def add_airtict(request):
    return  HttpResponse('文章')

def add_appmodel(request):
    cla = User.objects.filter(username='cla1136').first()
    permission = Permission.objects.filter(codename='add_appmodel').first()
    # cla.user_permissions.add(permission)

    # add_goup = Group.objects.create(name='add_group')
    add_group = Group.objects.filter(name='add_group').first()
    add_group.permissions.add(permission)
    add_group.user_set.add(cla)
    return HttpResponse('add_appmodel')