from django.db import models

# Create your models here.

# 数据库 》》 类
# 字段 》》  类属性

#1.定义类属性
class App(models.Model):
    app_id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=20)
    app_number = models.IntegerField()

# 2.生成映射文件
# python manage.py makemigrations [appname]

# 3.将映射文件数据提交到数据库
# python manage.py migrate [appname]


