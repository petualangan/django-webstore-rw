from django.shortcuts import render
from .models import * #import semua yang ada di models

# Create your views here.
# Mendefinisikan halaman web

def store(request):
    products = Product.objects.all() #nyimpen semua isi dari Product yang ada dimodel ke -> products
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context) # template store.html didalem folder store

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
