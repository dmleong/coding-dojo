from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

def index(request):
    location = ['San Jose', 'Mountain View', 'New York']
    language = ['Python', 'Javascript', "PHP"]
    context = {
        'locations': location,
        'languages' : language,
    }
    print context
    return render(request, 'surveys/index.html', context)

def process_form(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def view_result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }
    return render(request, 'surveys/result.html', context)
