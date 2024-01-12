from django.contrib import admin
from .models import Product, Category, Cart, Feature, Order, promocode

# Register your models here.

admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Cart),
admin.site.register(Feature),
admin.site.register(Order)
admin.site.register(promocode)
