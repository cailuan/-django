from django.shortcuts import render ,redirect ,reverse
from django.http import JsonResponse,HttpResponse
from .models import BlogModel
from django.views import View
from myFirstSubject.settings import MEDIA_ROOT
import os , datetime



# Create your views here.

def index(request):
    return render(request,'app_blog/index.html')

# def add(request):
#     if request.method == 'GET' :
#         pass
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         BlogModel.objects.create(title=title,content=content)
#     return  render(request,'app_blog/add.html')


def list(request):
    data = BlogModel.objects.all()
    return render(request,'app_blog/list.html',context={'data':data})

def add_article(request):
    return JsonResponse({'success':'true'})

def dele(request,id):
    dele_id = BlogModel.objects.get(id=id)
    if dele_id:
        dele_id.delete()
        return redirect(reverse('index'))
    else:
        return HttpResponse('删除失败')

class AddView(View):
    def get(self,request):
        return render(request,'app_blog/add.html')
    def post(self,request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogModel.objects.create(title=title,content=content)
        return render(request,'app_blog/add.html')



def detail(request,id):
    if request.method == 'GET':
        change = BlogModel.objects.get(id=id)
        return render(request,'app_blog/detail.html',context={'data':change})
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        data_id =BlogModel.objects.filter(id=id)
        print(data_id)
        if data_id:
            data_id.update(title=title,content=content)
        return redirect(reverse('index'))

def uploadfile(request):
    if request.method == 'GET':
        return render(request,'app_blog/uploadFile.html')
    if request.method == 'POST':
        filecontent = request.FILES['oneFile']
        # print(filecontent.chunks())
        f_name = os.path.join(MEDIA_ROOT,filecontent.name)
        with open(f_name,'wb') as f:
            for i in filecontent.chunks():
                f.write(i)
        # return render(request, 'app_blog/uploadFile.html')
        return HttpResponse('上传成功')

def set_cookie(request):
    request = HttpResponse('set cookie')
    # request.set_cookie('name','cla',max_age=100)
    request.set_cookie('name','cla',expires=datetime.datetime(2019,1,12,16,23))
    return request


def get_cookie(request):
    cookie = request.COOKIES
    name = cookie.get('name')
    return HttpResponse(name)

def remove_cookie(request):
    re = HttpResponse('移除cookie')
    re.delete_cookie('name')
    return re