from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from product.models import *
from django.contrib import messages


# Create your views here.
def home(request):
    # categories = Category.objects.all().filter(top)
    return render(request, 'core/index.html')

def shop(request):
    return render(request, 'core/shop-grid')

def add_to_cart(request):
    product = get_object_or_404(Product)
    order_item = Cart.objects.get_or_create(item=product, user=request.user, purchase=False)
    order_object = Order.object.filter(user=request.user, ordered=False)
    if order_object.exist():
        order = order_object[0]
        if order.orderitems.filter(item=product).exist():
            messages.success(request, "This product is already added in your cart.")
            return redirect('cart')
        else:
            order.orderitems.add(order_item[0])
            messages.success(request, "Product is added in your cart.")
            return redirect('cart')
        
    else: 
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.success(request, "Product is added in your cart")
        return redirect('cart')

def cart_view(request):
    # if request.user.is_authenticated:
    carts = Cart.objects.filter(user=request.user, purchase=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders.first()
        return render(request, 'core/cart.html', context={'carts':carts, 'orders':orders, 'order':order})
    else:
        messages.warning(request, "You don't have any items in your cart")
        return redirect('home')
    
    # else:
    #     # Handle the case where the user is not authenticated
    #     messages.warning(request, "Please log in to view your cart.")
    #     return redirect('user/login.html') 


def remove_from_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_obj = Order.objects.filter(user=request.user, ordered=False)
    if order_obj.exists():
        order = order_obj[0]
        if order.orderitems.filter(item=item).exist():
            order_item = Cart.objects.filter(item=item, user=request.user, purchase=False)
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This product is removed from your cart")
            return redirect("cart")
        else:
            messages.info(request, "You don't have an active order")
            return redirect("cart")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("home")

def checkout(request):
    return render(request, 'core/checkout.html')

def contact(request):
    return render(request, 'core/contact.html')


def webadmin(request):
    return render(request, 'webadmin/index.html')
