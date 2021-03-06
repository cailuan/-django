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
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asy/',view.sayHell),
    path('path/<path:paramse>',view.paramse),
    re_path('hello$/',view.hello),
    re_path('^repath$/(?P<yy>[0-9]?)',view.newPath,name='repath'),
    path('index/',include('app_book.urls'),{'switch':True}),
    path('appModel/',include('app_model.urls'),{'name':'cla'}),
    path('more/',include('more_table.urls')),
    path('blog/',include('blog.urls')),
    path('auth/',include('app_suth.urls'))
]
