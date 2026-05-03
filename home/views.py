from django.shortcuts import render, HttpResponse
from home.models import Contact
from .models import Product, Category
from django.core.paginator import Paginator

def index(request):
    # return HttpResponse("Here is teh first page")
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    featured_products = Product.objects.filter(is_featured=True)[:3]
    
    products = paginator.get_page(page_number)
    # return render(request, 'shop.html', {'products': products, 'categories': Category})
    return render(request, 'shop.html', {
        'products': products,
        'categories': categories,
        'featured_products': featured_products
    })

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('description')
        if name and email and desc:
            Contact.objects.create(
                name=name,
                email=email,
                description=desc
            )
        else:
            return HttpResponse("All fields are required")
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_use(request):
    return render(request, 'terms_of_use.html')

def sales_refund(request):
    return render(request, 'sales_refund.html')

def faq(request):
    return render(request, 'faq.html')

def international_order(request):
    return render(request, 'international_order.html')

def order_history(request):
    return render(request, 'order_history.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def return_policy(request):
    return render(request, 'return_policy.html')

def my_account(request):
    return render(request, 'my_account.html')

def about_us(request):
    return render(request, 'about_us.html')