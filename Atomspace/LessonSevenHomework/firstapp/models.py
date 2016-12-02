from django.db import models
import os
from django.contrib.auth.models import User

DIR_image = '/static/images/'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    avatar_image = models.CharField(default=DIR_image,null=True,max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField(auto_now=True)
    cover_image = models.FileField(upload_to='cover_image',null=True,blank=True)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User,related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')

class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile,related_name='voted_tickets')
    article = models.ForeignKey(to=Article,related_name='tickets')
    VOTE_CHOICES = (
        ('like','like'),
        ('dislike','dislike'),
        ('normal','normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICES,max_length=10)
    def __str__(self):
        return str(self.id)
