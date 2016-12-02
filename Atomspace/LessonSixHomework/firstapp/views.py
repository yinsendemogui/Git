from django.shortcuts import render,redirect
from firstapp.form import CommentForm
from firstapp.models import Article,Comment
from django.template import Context,Template

# Create your views here.




def detail(request):
    comment = {}
    article_list = Article.objects.all()
    comment_list = Comment.objects.all()
    form = CommentForm
    comment['article_list'] = article_list
    comment['comment_list'] =comment_list
    comment['form'] = form
    page_web = render(request,'detail.html',comment)
    return page_web



def detail_comment(request):
    form = CommentForm(request.POST)
    print (form)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        c = Comment(comment=comment)
        c.save()
        return redirect(to='detail')
    else:
        return detail(request)
