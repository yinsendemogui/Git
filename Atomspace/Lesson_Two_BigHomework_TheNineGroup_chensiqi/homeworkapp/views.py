#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from homeworkapp.models import Article, Comment, Ticket,UserProfile
from homeworkapp.forms import CommentForm,ProfileForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreation,Form, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    article_list = Article.objects.all()
    try:
        profile_list = UserProfile.objects.get(belong_to_id=request.user.id)
    except:
        profile_list = False
    page_robot = Paginator(article_list, 5)

    page_num = request.GET.get('page')
    print (page_num)
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
        
    context = {}
    context['profile_list'] = profile_list
    context["article_list"] = article_list

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    if request.method == "GET":
        form = CommentForm

    context = {}
    context["article"] = article
    context['form'] = form
    
    return render(request, 'detail.html', context)

def comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            comment = form.cleaned_data["comment"]
            article = Article.objects.get(id=id)
            c = Comment(name=name, comment=comment, belong_to=article)
            c.save()
            return redirect(to="detail", id=id)
    return redirect(to="detail", id=id)

def index_login(request):
    if request.method == "GET":
        form = LoginForm

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index")

    context = {}
    context['form'] = form

    return render(request, 'login.html', context)

def index_register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form

    return render(request, 'register.html', context)

def vote(request, id):
    # 未登录用户不允许投票，自动跳回详情页
    if not isinstance(request.user, User):
        return redirect(to="detail", id=id)

    voter_id = request.user.id

    try:
        # 如果找不到登陆用户对此篇文章的操作，就报错
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_this_article.choice = request.POST["vote"]
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=id, choice=request.POST["vote"])
        new_ticket.save()

    # 如果是点赞，更新点赞总数
    if request.POST["vote"] == "like":
        article = Article.objects.get(id=id)
        article.likes += 1
        article.save()

    return redirect(to="detail", id=id)

def Myinfo(request):
    context = {}
    if request.method == 'GET':

        try:
            profile_list = UserProfile.objects.get(belong_to_id = request.user.id)
            profile_list.password = '***********'
            form = ProfileForm(instance = profile_list)
        except:
            profile_list = False
            form = ProfileForm
        context['form'] = form
        context['profile_list'] = profile_list

        return render(request,'myinfo.html',context)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            password = form.cleaned_data['password']
            avatar_img = form.cleaned_data['avatar_img']
            try:
                f = UserProfile.objects.get(belong_to_id = request.user.id)
                f.name = name
                f.sex = sex
                f.password = password
                f.avatar_img = avatar_img

                # c = f(name=name, sex=sex, password=password, avatar_img=avatar_img)
                f.save()
            except:
                c = UserProfile(name=name, sex=sex, password=password, avatar_img=avatar_img,belong_to_id=request.user.id)
                c.save()
        request.user.set_password(password)
        request.user.save()
        return redirect(to='myinfo')


def Mycollection(request):
    context = {}
    voter_id = request.user.id  #当前登录用户的id号
    try:
        profile_list = UserProfile.objects.get(belong_to_id=request.user.id)   #取出属于登录用户的用户资料对象
    except:
        profile_list = False  #找不到说明没创建过
    article_like =Ticket.objects.filter(voter_id=voter_id,choice = 'like')   #找出属于当前登录用户的并且为like的投票对象（里面有对应的文章名称信息）
    article_list = []  #建立一个空列表
    for article in article_like:   # 将对象一个一个的迭代赋值给article
        article_list.append(Article.objects.get(title = article.article))    #  article.article是属于当前用户的并且点过赞（like）的文章的题目信息。
                                                                            #Article.objects.get(title = article.article)为找出文章models里文章题目等于article.article的文章对象
    page_robot = Paginator(article_list, 3)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context = {}

    context["article_list"] = article_list

    context['profile_list'] = profile_list
    return render(request, 'mycollection.html', context)

