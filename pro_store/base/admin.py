from django.contrib import admin
from .models import Product, Category, OrderItem, ShippingAddress, Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
