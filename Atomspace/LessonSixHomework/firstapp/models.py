from django.db import models

# Create your models here.


class Article(models.Model):
    headline = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    def __str__(self):
        return self.headline



class Comment(models.Model):
    name = models.CharField(default='chensiqi',max_length=10)
    comment = models.TextField(max_length=500)
    avatar = models.CharField(default='http://semantic-ui.com/images/avatar/small/matt.jpg',max_length=50)
    createtime = models.DateField(auto_now=True)
    def __str__(self):
        return self.comment
