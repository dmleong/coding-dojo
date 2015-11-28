from django.shortcuts import render, redirect
import random
import datetime
from .forms import farmForm, houseForm, casinoForm, caveForm

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if not request.session.get('activity', None):
        request.session.setdefault('activity', [0])

    context = {
        'counter' : request.session['counter'],
        'activities': request.session['activity'],
        'farmForm': farmForm(),
        'houseForm': houseForm(),
        'casinoForm': casinoForm(),
        'caveForm': caveForm(),
    }
    return render(request, 'home/index.html', context)

def randomNum(start, end):
    num = random.randrange(start, end)
    return num

def addActivity(request, num, action, location):
    timestamp = datetime.datetime.now()
    if not request.session.get('activity', None):
        activities = []
    else:
        activities = request.session['activity']
    print activities
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %s from the casino! %s' % (num, timestamp)
            activities.insert(0, ['earn', earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %s gold... Ouch %s' % (num, timestamp)
            activities.insert(0, ['lost', lost])
        else:
            print "error"
    elif location == 'farm':
        activities.insert(0, ['earn', 'Earned %s from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        activities.insert(0, ['earn', 'Earned %s from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        activities.insert(0, ['earn', 'Earned %s from the %s! %s' % (num, location, timestamp)])
    else:
        print "error"
    request.session['activity'] = activities

def earnOrAdd():
    chance = randomNum(0, 2)
    if chance == 1:
        return True
    else:
        return False

def process_money(request):
    if request.POST['hidden'] == 'farm':
        farmNum = randomNum(10, 21)
        request.session['counter'] += farmNum
        addActivity(request, farmNum, 'earned', 'farm')
    elif request.POST['hidden'] == 'cave':
        caveNum = randomNum(5, 10)
        request.session['counter'] += caveNum
        addActivity(request, caveNum, 'earned', 'cave')
    elif request.POST['hidden'] == 'house':
        houseNum = randomNum(2, 5)
        request.session['counter'] += houseNum
        addActivity(request, houseNum, 'earned', 'house')
    elif request.POST['hidden'] == 'casino':
        casinoNum = randomNum(0, 50)
        chance = earnOrAdd()
        if chance == True:
            request.session['counter'] += casinoNum
            addActivity(request, casinoNum, 'earned', 'casino')
        elif chance == False:
            request.session['counter'] -= casinoNum
            addActivity(request, casinoNum, 'lost', 'casino')
        else:
            print "Error"
    else:
        print "Error"
    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
