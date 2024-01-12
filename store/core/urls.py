from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart_view, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('checkout/', views.checkout, name="checkout"),


    # admin routes
    path('webadmin/', views.webadmin)
   
]