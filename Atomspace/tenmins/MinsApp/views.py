from django.shortcuts import render,HttpResponse
from django.template import Context,Template

# Create your views here.



def index(request):
    context = {}
    index_page = render(request,'list.html',context)
    return index_page


def radio(request):
    context = {}
    index_page = render(request, 'Request-Get.html', context)
    return index_page