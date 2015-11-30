from django.shortcuts import *
from django.views.generic import View
from django.http import HttpResponse

class MyView(View):
    def get(self, response):
        return render(response, 'message/index.html')
    def post(self, request):
        return HttpResponse('Message submitted')
