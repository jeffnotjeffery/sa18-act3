import json
from django.shortcuts import render
from .models import Product

def index(request):
    with open('myapp/fixtures/products.json') as json_file:  # Corrected path to fixtures folder
        products = json.load(json_file)
    return render(request, 'myapp/index.html', {'products': products})

def show(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'myapp/show.html', {'product': product})
