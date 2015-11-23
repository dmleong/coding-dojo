from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
def index(request):
    context = {
        'person': [
            {'name': 'Danielle', 'sport': 'rock climbing', 'language': 'Python'},
        ]
    }

    return render(request, 'home/index.html', context) # updated this line
