"""myFirstSubject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path , include
from . import views

urlpatterns = [
    path('index.html',views.index,name='index'),
    # path('add.html',views.add,name='add'),
    path('add.html',views.AddView.as_view(),name='add'),
    path('list.html',views.list,name='list'),
    path('detail/<id>',views.detail,name='detail'),
    path('dele/<id>',views.dele,name='dele'),
    path('addArticla',views.add_article),
    path('uploadfile',views.uploadfile,name='upload'),
    path('set_cookie',views.set_cookie),
    path('get_cookie',views.get_cookie),
    path('remove_cookie',views.remove_cookie)
]