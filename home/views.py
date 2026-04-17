from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("Here is teh first page")
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

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