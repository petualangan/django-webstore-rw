from django.shortcuts import render
from .models import * #import semua yang ada di models
from django.http import JsonResponse
import json

# Create your views here.
# Mendefinisikan halaman web

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []  # kalo nggak, itemnya kosong
        order = {'get_cart_total': 0,'get_cart_items': 0}  # percobaan kalau logout (ngga ada user login di localhost/admin), efeknya halaman cart akan kosong
        cartItems = order['get_cart_items']

    products = Product.objects.all() #nyimpen semua isi dari Product yang ada dimodels ke -> products

    context = {
        'products': products,
        'cartItems': cartItems
    }

    return render(request, 'store/store.html', context) # template store.html didalem folder store

def cart(request):
    #kalau usernya login
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [] #kalo nggak, itemnya kosong
        order = {'get_cart_total': 0, 'get_cart_items': 0} #percobaan kalau logout (ngga ada user login di localhost/admin), efeknya halaman cart akan kosong
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0} #percobaan kalau logout (ngga ada user login di localhost/admin), efeknya halaman cart akan kosong
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body) # bodynya yang ada di cart.js
    productId = data['productId']
    action = data['action'] # logicnya udah di buat di cart.js
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False) # kalo tombol add to cart ditekan, akan menghubungkan dari order ke customer

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product) # menghubungkan orderItem ke variable order(isinya order) diline atas, begitu juga product

    # membuat quantity di cart.html bekerja, BUKAN tombol panah naek/turun-nya
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False) # memberikan return berupa Json