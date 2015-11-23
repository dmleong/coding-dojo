from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.now().date().strftime('%B %-d, %Y')
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request, 'times/index.html', context) # updated this line
