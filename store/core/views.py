from django.shortcuts import render
from product.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    # categories = Category.objects.all().filter(top)
    return render(request, 'core/index.html')

def shop(request):
    return render(request, 'core/shop-grid')

def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchase=False)
    orders = Order.object.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = order[0]
        return render(request, 'core/cart.html', context={'carts':carts, 'order':order, 'orders':orders})
    else:
        messages:warning(request, "You don't have any items in your cart")
        return redirect('home')

def checkout(request):
    return render(request, 'core/checkout.html')

def contact(request):
    return render(request, 'core/contact.html')


def webadmin(request):
    return render(request, 'webadmin/index.html')
