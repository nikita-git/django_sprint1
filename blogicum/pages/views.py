from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


# def about(request):
    # template = 'pages/about'
    # return render(request, template)
# 
# 
# def rules(request):
    # template = 'pages/rules'
    # return render(request, template)


def about(request):
    return HttpResponse('О нас')


def rules(request):
    return HttpResponse('Правила')
