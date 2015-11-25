from django.http import HttpResponse, Http404
from django.shortcuts import render
from apps.interests.models import Interest, User      # inserted this line which import our app's models

def show_interests(request):
    users = User.objects.all()
    interests = Interest.objects.all()
    context = {
        "users" : users,
        "interests" : interests,
    }
    print context
    return render(request, 'interests/index.html', context)

def show_user(request, id):
    users = User.objects.get(id=id)
    context = {
        "users": users,
    }
    return render(request, 'interests/user.html', context)
