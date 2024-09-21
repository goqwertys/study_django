from django.http import HttpResponse

from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, 'base.html')


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'latest_products': latest_products})

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Thanks, {name}! Message received.')
    return render(request, 'contacts.html')
