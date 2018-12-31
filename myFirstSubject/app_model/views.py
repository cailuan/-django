from django.shortcuts import render
from django.http import HttpResponse
from .models import AppModel


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