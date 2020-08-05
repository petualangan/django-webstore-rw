from django.shortcuts import render
from .models import * #import semua yang ada di models

# Create your views here.
# Mendefinisikan halaman web

def store(request):
    products = Product.objects.all() #nyimpen semua isi dari Product yang ada dimodels ke -> products
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context) # template store.html didalem folder store

def cart(request):
    #kalau usernya login
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = [] #kalo nggak, itemnya kosong
        order = {'get_cart_total': 0, 'get_cart_items': 0} #percobaan kalau logout (ngga ada user login di localhost/admin), efeknya halaman cart akan kosong

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0} #percobaan kalau logout (ngga ada user login di localhost/admin), efeknya halaman cart akan kosong

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)
