from django.db import models

# Create your models here.

class BlogModel(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=30)