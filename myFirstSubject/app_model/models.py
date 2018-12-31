from django.db import models

# Create your models here.

class AppModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return 'AppModel id = %s , name = %s , age = %s' %(self.id,self.name,self.age)

