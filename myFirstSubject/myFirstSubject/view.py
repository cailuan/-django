from django.http import HttpResponse

def sayHell(request):
    return HttpResponse('hello world this is first django project')

def paramse(request,paramse):
    return  HttpResponse('这是动态路由 %s' %paramse)

def hello(request):
    return HttpResponse('hello world')

def newPath(request,yy):
    return HttpResponse('正则表达式 %s' %yy)