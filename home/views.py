from django.shortcuts import render, HttpResponse, redirect
from .models import Contact

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
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('contact')  # reload page or show success msg

    return render(request, 'contact.html')