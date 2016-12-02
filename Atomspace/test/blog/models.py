from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    # 用户姓名
    name = models.CharField(null=True, blank=True, max_length=14)
    # 用户邮箱
    email = models.EmailField(null=True)
    # 用户描述信息
    desc = models.CharField(null=True, blank=True, max_length=250, default='未添加描述')
    # 用户头像
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    # 话题名称
    name = models.CharField(null=True, blank=True, max_length=14)
    def __str__(self):
        return self.name

class Question(models.Model):
    # 问题提出者
    author = models.ForeignKey(to=UserProfile, related_name='question_author')

    # 问题标题
    title = models.CharField(null=True, blank=True, max_length=100)

    # 问题描述
    desc = models.CharField(null=True, blank=True, max_length=1000)

    # 话题列表
    topics = models.ManyToManyField(Topic)

    # 回答数目
    answer_counts = models.IntegerField(default=0)

    # 问题创建时间
    createtime = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    # 回答所属问题
    question =  models.ForeignKey(to=Question, related_name='question_answer')

    # 回答者
    author = models.ForeignKey(to=UserProfile, related_name='answer_author')

    # 回答内容
    content = models.TextField(null=True, blank=True)

    # 赞同数目
    like_counts = models.IntegerField(default=0)

    # 不赞同数目
    dislike_counts = models.IntegerField(default=0)

    # 评论数目
    comment_counts = models.IntegerField(default=0)

    # 回答创建时间
    createtime = models.DateField(auto_now=True)


class Comment(models.Model):
    # 评论者
    author = models.ForeignKey(to=UserProfile, related_name='comment_author')

    # 评论所属回答
    answer = models.ForeignKey(to=UserProfile, related_name='answer_comment')

    # 评论内容
    content = models.TextField(null=True, blank=True)

    # 评论时间
    createtime = models.DateField(auto_now=True)


class Ticket(models.Model):
    '''
    投票modes实现
    autor：徐毅
    '''
    voter = models.ForeignKey(to=User, related_name="user_tickets")
    answer_tickets = models.ForeignKey(to=Answer, related_name="answer_tickets")

    ARTICLE_CHOICES = {
        ("like", "like"),
        ("dislike", "dislike"),
        ("normal", "normal")
    }
    choice = models.CharField(choices=ARTICLE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)