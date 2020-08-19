import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)
    items = []  # kalo nggak, itemnya kosong
    order = {'get_cart_total': 0,
             'get_cart_items': 0}  # percobaan kalau logout (ngga ada user login di localhost/admin), efeknya halaman cart akan kosong
    cartItems = order['get_cart_items']

    try:
        for i in cart:
            cartItems += cart[i][
                'quantity']  # ditambah sama quantitiy, tiap product dibedakan sama id nya (kalau ngga salah sih gitu pemahamanku)

            # render total harganya -> biar muncul di cart.html
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            # render itemnya
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True
    except:
        pass

    return {'cartItems': cartItems, 'order':order, 'items': items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)  # request dari utils.py
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order':order, 'items': items}