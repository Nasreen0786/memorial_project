from django.contrib import admin
from django.urls import path
from home import views
from home.views import contact_view

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('contact/', contact_view, name='contact'),
]