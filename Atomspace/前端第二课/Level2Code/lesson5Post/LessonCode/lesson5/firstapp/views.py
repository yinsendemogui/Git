from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import Aritcle, Comment
from django.template import Context, Template
from firstapp.form import CommentForm

def index(request):
    print(request)
    print('==='*30)
    print(dir(request))
    print('==='*30)
    print(type(request))
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Aritcle.objects.filter(tag=queryset)
    else:
        article_list = Aritcle.objects.all()
    context = {}
    context['article_list'] = article_list
    print(article_list)
    index_page = render(request, 'first_web_2.html', context)
    return index_page


def detail(request):
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # print(form.errors)
        # print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            a = Aritcle.objects.get(id=page_num)
            c = Comment(name=name, comment=comment)
            c.save()
            return redirect(to='detail')

    context = {}
    comment_list = Comment.objects.all()
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'article_detail.html', context)
