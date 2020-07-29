from django.urls import path
from . import views # ngambil dari modul views.py

urlpatterns = [
    path('', views.store, name='store'), # karena home, jadi alamat webnya udah kosongin aja. kan nanti namadomain.com gitu
    path('cart/', views.cart, name='cart'), # cart/ -> alamat webnya, jadinya -> namadomain.com/cart/ | pakai localhost -> http://127.0.0.1:8000/cart/
    path('checkout/', views.checkout, name='checkout'), #vies.checkout -> modul views -> checkout -> kan ngerender checkout.html
]


#file urls ini, isinya halaman web yang kita tambahin bebas, tpi perlu didaftarin dulu di urls.py yang ada didalaman folder ecommerce