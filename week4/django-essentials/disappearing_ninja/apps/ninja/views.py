from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    context = {
        'view_all': False,
    }
    return render(request, 'ninja/index.html', context)

def all(request):
    context = {
        'view_all': True,
    }
    return render(request, 'ninja/index.html', context)

def ninja(request, color):
    if color == 'blue' or color == 'red' or color == 'purple' or color == 'orange':
        context = {
            'view_all' : False,
            'color': color,
        }
    else:
        context = {
            'view_all': False,
            'april': True,
        }
    return render(request, 'ninja/index.html', context)
