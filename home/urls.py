from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_of_use', views.terms_of_use, name='terms_of_use'),
    path('sales_refund', views.sales_refund, name='sales_refund'),
    path('faq', views.faq, name='faq'),
    path('international_order', views.international_order, name='international_order'),
    path('order_history', views.order_history, name='order_history'),
    path('wishlist', views.wishlist , name='wishlist ,'),
    path('return_policy', views.return_policy, name='return_policy'),
    path('my_account', views.my_account, name='my_account'),
    path('about_us', views.about_us, name='about_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)