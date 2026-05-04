from django.shortcuts import render, HttpResponse
from home.models import Contact
from .models import Product, Category
from django.core.paginator import Paginator

def index(request):
    # return HttpResponse("Here is teh first page")
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category


from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category


def shop(request):

    categories = Category.objects.all()

    products = Product.objects.all()

    # Category Filter
    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    # Featured Products
    featured_products = Product.objects.filter(is_featured=True)[:3]

    # Pagination AFTER filtering
    paginator = Paginator(products, 6)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)

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