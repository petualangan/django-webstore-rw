from django.shortcuts import render

# Create your views here.
# Mendefinisikan halaman web

def store(request):
    context = {}
    return render(request, 'store/store.html', context) # template store.html didalem folder store

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
