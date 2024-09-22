from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:products')  # Перенаправление на страницу со списком товаров
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
