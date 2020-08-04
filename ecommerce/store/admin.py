from django.contrib import admin
from .models import * # mendaftarkan model(semua class-nya) ke admin

# Register your models here.
admin.site.register(Customer) # Customer -> class yang ada di file models.py
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)