from django.shortcuts import render,HttpResponse,redirect
from firstapp.models import People,Aritcle,Comment
from django.template import Context,Template
from firstapp.form import CommentForm

# Create your views here.
def first_try(request):
    person = People(name = 'spock',job = 'officer')
    html_string ='''
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css"
                <link rel="stylesheet" href="css/semantic.css" media="screen" title="no title">
                media="screen" title="no title">
                <title>Title</title>
            </head>
            <body>
            <h1 class = "ui center aligned icon header">
                <i class = "hand spock icon"></i>
                hello,{{ person.name }}
            </h1>
            </body>
        </html>
    '''
    t = Template(html_string)
    c = Context({'person': person})
    web_page = t.render(c)
    return HttpResponse(web_page)

def index(request):
    print(request)
    print('==='*30)
    print(dir(request))
    print('==='*30)
    print(type(request))
    queruset = request.GET.get('tag')

    if queruset:
        article_list = Aritcle.objects.filter(tag=queruset)
    else:
        article_list = Aritcle.objects.all()
    context = {}
    # article_list = Aritcle.objects.all()
    context['article_list'] = article_list
    index_page = render(request,'first_web_2.html',context)
    return index_page


def detail(request,page_num,error_form=None):

    context = {}
    form = CommentForm
    a = Aritcle.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
    if best_comment:
        context['best_comment'] = best_comment[0]
    article = Aritcle.objects.get(id=page_num)
    context['article'] = article
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    detail_page = render(request, 'article_detail.html', context)
    return detail_page

def detail_comment(request,page_num):

    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        a = Aritcle.objects.get(id=page_num)
        c = Comment(name=name, comment=comment, belong_to=a)
        c.save()
    else:
        return detail(request,page_num,error_form=form)
    return redirect(to='detail', page_num=page_num)