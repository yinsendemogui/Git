from django.shortcuts import render,HttpResponse,redirect
from firstapp.models import Article,Ticket
from firstapp.form import LoginForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def listing(request,cate = None):
    context = {}
    if cate is None:
        article_list = Article.objects.all()
    elif cate == 'editors':
        article_list = Article.objects.filter(editors_choice = True)
    else:
        article_list = Article.objects.all()

    page_robot = Paginator(article_list,5)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context["article_list"] = article_list
    return render(request, 'list.html', context)

def detail(request,id):
    context = {}
    article_info = Article.objects.get(id=id)
    voter_id = request.user.profile.id
    user_ticket_for_this_article = Ticket.objects.get(voter_id = voter_id,article_id = id)
    context['user_ticket'] = user_ticket_for_this_article
    context['article_info'] = article_info
    return render(request,'detail.html',context)

def detail_vote(request,id):
    voter_id = request.user.profile.id
    try:
        user_ticker_for_this_article = Ticket.objects.get(voter_id = voter_id,article_id = id)
        user_ticker_for_this_article.choice = request.POST['vote']
        user_ticker_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id,article_id=id,choice=request.POST['vote'])
        new_ticket.save()

    return redirect(to='detail',id=id)

def login_index(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect(to = 'list')
            # else:
            #     return HttpResponse('<h1>没有这个用户！</h1>')
    context['form'] = form
    return render(request,'register_index.html',context)

def register_index(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request,'register_index.html',context)

