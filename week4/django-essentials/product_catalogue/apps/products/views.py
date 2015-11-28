from django.shortcuts import *
from django.forms.models import inlineformset_factory
from apps.products.models import Product
from .forms import ProductForm, ProductIdForm
from datetime import datetime
from django.template import RequestContext

# Create your views here.
def index(response):
    products = Product.objects.all()
    form = ProductForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(response, 'products/index.html', context)

def create_product(request):
    data = {
        'brand_name': request.POST['brand_name'],
        'product_name': request.POST['product_name'],
        'price': request.POST['price'],
        'description': request.POST['description'],
    }

    if request.method == 'POST':
        form = ProductForm(data)
        products = Product.objects.all()

        if form.is_valid():
            form.process()
            return HttpResponseRedirect('/')
        else:
            form_errors = form.errors
            context = {
                'products': products,
                'form': form,
                'errors': form_errors,
            }
            return render_to_response('products/index.html', context, context_instance=RequestContext(request))
    return redirect('/')

def edit_product(request, id):
    products = Product.objects.get(id=id)
    request.session['id'] = products.id
    request.session['product_name'] = products.product_name
    request.session['brand_name'] = products.brand_name
    request.session['price'] = products.price
    request.session['description'] = products.description
    form = ProductIdForm(request)
    context = {
        'id': id,
        'form': form,
    }
    return render_to_response('products/edit.html', context, context_instance=RequestContext(request))

def update_product(request, id):
    data = {
        'brand_name': request.session['brand_name'],
        'product_name': request.POST['product_name'],
        'price': request.POST['price'],
        'description': request.POST['description'],
    }

    if request.method == 'POST':
        form = ProductIdForm(request, data)
        if form.is_valid():
            form.update(id)
            return HttpResponseRedirect('/')
        else:
            form_errors = form.errors
            context = {
                'form': form,
                'errors': form_errors,
            }
            return render_to_response('products/edit.html', context, context_instance=RequestContext(request))
    return redirect('/')

def delete_product(request, id):
    form = ProductIdForm(request)
    form.delete(id)
    return redirect('/')
