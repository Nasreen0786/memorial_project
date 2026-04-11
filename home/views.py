from django.shortcuts import render, HttpResponse

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