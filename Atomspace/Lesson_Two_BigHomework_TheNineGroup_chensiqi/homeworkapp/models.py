#!/usr/bin/python
# -*- coding: utf-8 -*-



from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(default='/static/images/',null=True, blank=True, max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=500)
    avatar = models.CharField(max_length=250, default="static/images/default.png")
    comment = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)

    belong_to = models.ForeignKey(to=Article, related_name="under_comments", null=True, blank=True)
    
    def __str__(self):
        return self.name

class Ticket(models.Model):
    voter = models.ForeignKey(to=User, related_name="user_tickets")
    article = models.ForeignKey(to=Article, related_name="article_tickets")

    ARTICLE_CHOICES = {
        ("like", "like"),
        ("dislike", "dislike"),
        ("normal", "normal")
    }
    choice = models.CharField(choices=ARTICLE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    CHOICE = (
        ('性别','性别'),
        ('男','男'),
        ('女','女')
    )
    sex = models.CharField(choices=CHOICE,max_length=10)
    password = models.CharField(null=True,blank=True,max_length=50)
    avatar_img = models.ImageField(upload_to='avatar_img',null=True,blank=True)
    belong_to = models.ForeignKey(to=User,related_name='userprofile',null=True,blank=True)
    def __str__(self):
        return str(self.belong_to_id)