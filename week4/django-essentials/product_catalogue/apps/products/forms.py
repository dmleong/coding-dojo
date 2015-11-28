from django import forms
from django.shortcuts import *
from datetime import datetime
from apps.products.models import Product

class ProductForm(forms.Form):
    all_choices = Product.objects.all()
    choices = []
    for choice in all_choices:
        choices.append((choice.brand_name, choice.brand_name))

    brand_name = forms.ChoiceField(widget=forms.Select(attrs={'required': True, 'class': 'form-control'}), choices=choices)
    product_name = forms.CharField(label="Product Name", max_length=200, widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'required': True, 'class': 'form-control'}))

    def process(self):
        product = self.cleaned_data
        new_product = Product.objects.create(brand_name=product['brand_name'], product_name=product['product_name'], price=product['price'], description=product['description'], created_at=datetime.now())


class ProductIdForm(forms.Form):
    def __init__(self,request,*args,**kwargs):
        super (ProductIdForm,self).__init__(*args,**kwargs)
        self.fields['brand_name'] = forms.CharField(label='Brand Name', initial=request.session['brand_name'], widget=forms.TextInput(attrs={'disabled': True, 'class': 'form-control'}))
        self.fields['product_name'] = forms.CharField(label='Product Name',max_length=200,initial=request.session['product_name'], widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
        self.fields['price'] = forms.CharField(label='Price', initial=request.session['price'], widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
        self.fields['description'] = forms.CharField(label="Description", initial=request.session['description'], widget=forms.Textarea(attrs={'required': True, 'class': 'form-control'}))

    def update(self, id):
        edited_product = self.cleaned_data
        updated_product = Product.objects.get(id=id)
        updated_product.product_name = edited_product['product_name']
        updated_product.price = edited_product['price']
        updated_product.description = edited_product['description']
        updated_product.save()

    def delete(self, id):
        delete_product = Product.objects.get(id=id).delete()
