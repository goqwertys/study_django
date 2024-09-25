from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product, FeedBackMessage
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

# Create your views here.
# def product_list(request):
#     """ Page with all products """
#     product_list = Product.objects.all()
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(product_list, 10)
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
#
#     context = {
#         'products': products
#     }
#     return render(request, 'product_list.html', context)

# def product_detail(request, pk):
#     """ Product detail page """
#     product = get_object_or_404(Product,pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'product_detail.html', context)


class ProductDetailView(DetailView):
    """ Product detail page """
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class HomeProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()[:5]

# def home(request):
#     """ Home page with 5 latest products """
#     latest_products = Product.objects.order_by('-created_at')[:5]
#     context = {
#         'products': latest_products
#     }
#     return render(request, 'home.html', context)
class ContactsCreateView(CreateView):
    """ Page for Contacts with Feedback message feature """
    model = FeedBackMessage
    fields = ['name', 'phone', 'message']
    template_name = 'contacts.html'
    success_url = reverse_lazy('catalog:feedback_success')


class FeedBackMessageSent(TemplateView):
    template_name = 'feedback_success.html'


# def contacts(request):
#     """ Page with contact info """
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f'Thanks, {name}! Message received.')
#     return render(request, 'contacts.html')

class AddProduct(CreateView):
    model = Product
    fields = ['name', 'description', 'pic', 'price']
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:product_created')

class ProductCreated(TemplateView):
    template_name = 'product_created.html'

def add_product(request):
    """ Page with add product form """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
