from django.shortcuts import render
from .models import * #import semua yang ada di models
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder

# Create your views here.
# Mendefinisikan halaman web

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all() #nyimpen semua isi dari Product yang ada dimodels ke -> products

    context = {
        'products': products,
        'cartItems': cartItems
    }

    return render(request, 'store/store.html', context) # template store.html didalem folder store

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

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

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body) # request ke body, ada dibagian script -> checkout.html

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])  # data itu variable yang dibuat diatas itu | form ada dibagian script -> checkout.html
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True  # dihalaman admin sih ini, ada di bagian order checkbox complete
    order.save()

    if order.shipping == True:  # kalo barang butuh dikirim
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],# ambil data nya, ambil shipping -> script di checkout.html, ambil addressnya
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )
    return JsonResponse('Payment complete!', safe=False)