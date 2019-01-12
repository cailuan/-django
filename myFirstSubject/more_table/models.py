from django.db import models

# Create your models here.

class Student(models.Model):
    s_name = models.CharField(max_length=30)
    s_id = models.AutoField(primary_key=True)
    deparment = models.ForeignKey('Deparment',on_delete=models.CASCADE)
    def __str__(self):
        return '%s id %s name %s departement' %(self.s_id,self.s_name,self.deparment_id)


class Deparment(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30)
    create_date = models.DateField(auto_now_add=True)


class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30)
    student = models.ManyToManyField('Student',related_name='students')
    def __str__(self):
        return 'id = %s name = %s student = %s'%(self.c_id,self.c_name,self.student.all())

class Student_Detail(models.Model):
    sd_id = models.OneToOneField('Student',on_delete=models.CASCADE)
    gender = models.BooleanField(default=True)
    modify_time = models.DateTimeField(auto_now=True)