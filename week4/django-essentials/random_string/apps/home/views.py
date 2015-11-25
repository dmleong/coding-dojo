from django.shortcuts import render, redirect
import string
import random

# Create your views here.
def index(request):
    new_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    # if request.session.get('counter', False):
    #     request.session['counter'] = 1
    #     print "counter", request.session['counter']
    if 'counter' not in request.session:
        request.session['counter'] = 1
        print "counter inside", request.session['counter']
    print "counter outside", request.session['counter']
    context = {
        'string': new_string,
        'counter': request.session['counter'],
    }
    return render(request, 'home/index.html', context)

def increment(request):
    request.session['counter'] += 1
    return redirect('/')

def clear(request):
    try:
        request.session['counter'] = 1
    except KeyError:
        pass
    return redirect('/')
