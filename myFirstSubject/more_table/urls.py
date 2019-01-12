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
   path('index/',views.more_index),
   path('add-department/',views.add_department),
   path('add-student/',views.add_student),
   path('add-student-detail',views.add_studennt_detail),
   path('add-coures',views.add_course),
   path('add_course_student',views.add_course_student),
   path('query_test',views.query_test),
   path('json',views.query_fun)
]