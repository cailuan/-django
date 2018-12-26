from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.template.loader import get_template
import datetime

# Create your views here.
def viewFun(request,**kwargs):
    if kwargs.get('switch'):
        return HttpResponse('new page ' )

def lastFun(request,**kwargs):
    return redirect(reverse('old'))

def oldFun(request,**kwargs):
    return redirect('/index/index')

def templateFun(request,**kwargs):
    t = get_template('app_book/index.html')
    html = t.render({'name':kwargs})
    # return render(request,'app_book/index.html')
    return HttpResponse(html)

def staticFile(request,**kwargs):
    return render(request,'app_book/static.html',
                  context={'now':datetime.datetime.now(),
                           'word':'<h1>this is one day , say hello world</h1>',
                           'newList':['a','b','c','v','n',' '],
                           'oldList':[],
                           'kw':kwargs,
                           'boolean':False
                           })

def base(request,**kwargs):
    return render(request,'app_book/base.html')

def super(request,**kwargs):
    return render(request,'app_book/super.html')

def parents(request,**kwargs):
    return render(request,'app_book/parents.html')