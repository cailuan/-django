from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Deparment,Student,Student_Detail,Course
from django.db.models import Avg,Count,Max,Min,Sum
# Create your views here.

def more_index(request):
    return HttpResponse('index')

def add_department(request):
    Deparment.objects.create(d_name='C')
    Deparment.objects.create(d_name='java')
    Deparment.objects.create(d_name='pathon')
    Deparment.objects.create(d_name='javascript')
    return  HttpResponse('add_department')

def add_student(request):
    Student(s_name='cla',deparment_id=1).save()
    Student(s_name='an',deparment_id=2).save()
    Student(s_name='cai',deparment_id=3).save()
    Student(s_name='luan',deparment_id=3).save()
    return HttpResponse('add_student')

def add_studennt_detail(request):
    # cla = Student_Detail()
    # cla.gender = True
    # cla.sd_id_id = 1
    # cla.save()
    an = Student_Detail()
    an.gender = False
    an.sd_id_id = 2
    an.save()
    cai = Student_Detail()
    cai.gender = False
    cai.sd_id_id = 3
    cai.save()
    luan = Student_Detail()
    luan.gender = False
    luan.sd_id_id = 4
    luan.save()
    return HttpResponse('add_student_detail')

def add_course(request):
    Course.objects.get_or_create(c_name='计算机基础')
    Course.objects.get_or_create(c_name='前端框架')
    Course.objects.get_or_create(c_name='数据库')
    Course.objects.get_or_create(c_name='数据分析')

    return HttpResponse('add_course')

def add_course_student(request):
    javascrippt = Course.objects.get(c_name='前端框架')
    s1 = Student.objects.get(s_id=1)
    s2 = Student.objects.get(s_id=2)
    s3 = Student.objects.get(s_id=3)
    c6 = Course.objects.get(c_id=6)
    s4 = Student.objects.get(s_id=4)
    javascrippt.student.add(s3)
    # s4.course_set.create(c_name='电子设备')
    computer_base = Course.objects.get(c_name='计算机基础')
    computer_base.student.add(s1)
    # s2.course_set.add(computer_base) 现在related_name='students' 所以course_set 不能用
    s2.students.add(computer_base)
    # s1.students.clear()
    # s4.students.remove(c6)
    return HttpResponse('add_course_student')

def query_test(request):
    # stu1 = Student.objects.get(s_id=1)
    # cou1 = Course.objects.get(c_id=1)
    # dep1 = Deparment.objects.get(d_id=3)
    # stu_det1 = Student_Detail.objects.get(sd_id=1)
    # print(stu1.deparment,stu1.deparment_id,dep1.student_set.all(),cou1.student.all())
    # print(stu1.students.all(),dep1.student_set.all())
    # print(stu1.student_detail,stu_det1.sd_id)
    ss = Student.objects.filter(deparment__d_id=1)
    nn = Student.objects.filter(students__c_id=1)
    mm = Course.objects.filter(student__deparment__d_id=1)
    print(ss,nn,mm)
    return HttpResponse('query')

def query_fun(request):
    return JsonResponse({'name':'1'})