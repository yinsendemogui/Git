from django.db import models
import os

os.path.dirname(__file__)
IMAGE_DIR = os.path.dirname(os.path.abspath(__file__))+'/static/images/default.png'
IMAGE_DIR = IMAGE_DIR.replace('\\','/')


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    print (IMAGE_DIR)
    name = models.CharField(max_length=10)
    avatar = models.CharField(default=IMAGE_DIR,max_length=100)
    content = models.TextField(null=True,blank=True)
    createtime = models.DateField(auto_now=True)
    def __str__(self):
        return self.content
