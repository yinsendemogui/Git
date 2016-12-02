from django.shortcuts import render
from django.template import Context,Template
from secondweb.models import Article


# Create your views here.


def index(request):
    context ={}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    web_page = render(request,'l6h1.html',context)
    return web_page