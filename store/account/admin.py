from django.contrib import admin
from .models import CustomUser, Address, Order, Staff

# Register your models here.

admin.site.register(CustomUser),
admin.site.register(Address),
admin.site.register(Order),
admin.site.register(Staff),