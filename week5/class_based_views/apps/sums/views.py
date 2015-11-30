from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured


class Main(View):
    def __init__(self):
        self.template = ''
        self.favorite_number = None
        self.least_favorite_number = None
        self.sum = ''
        self.difference = ''
        self.product = ''
        self.factor = ''

    def get(self, request):
        context = {
            'sum': self.add(
                self.favorite_number,
                self.least_favorite_number,
            ),
            'difference': self.subtract(
                self.favorite_number,
                self.least_favorite_number,
            ),
            'product': self.multiply(
                self.favorite_number,
                self.least_favorite_number,
            ),
            'factor': self.divide(
                self.favorite_number,
                self.least_favorite_number,
            ),
        }
        return render(request, self.get_template(), context)

    def get_template(self):
        if self.template == '':
            raise ImproperlyConfigured('"Template" not defined.')
        return self.template

    def add(self, favorite_number, least_favorite_number):
        self.sum = self.favorite_number + self.least_favorite_number
        return self.sum

    def subtract(self, favorite_number, least_favorite_number):
        self.difference = self.favorite_number - self.least_favorite_number
        return self.difference

    def multiply(self, favorite_number, least_favorite_number):
        self.product = self.favorite_number * self.least_favorite_number
        return self.product

    def divide(self, favorite_number, least_favorite_number):
        self.factor = self.favorite_number / self.least_favorite_number
        return self.factor


class Calculator(Main, View):
    def __init__(self):
        super(Calculator, self).__init__()
        self.template = 'sums/index.html'
        self.favorite_number = 24
        self.least_favorite_number = 7
