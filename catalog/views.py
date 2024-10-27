from itertools import product

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation.trans_real import catalog
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib import messages

from catalog.forms import ProductForm
from catalog.models import Product, FeedBackMessage


@permission_required('catalog.can_unpublish_product')
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.status = 'DR'
    product.save()
    messages.success(request, 'Product has unpublished successfully')
    return redirect('catalog:product_list')


@permission_required('catalog.can_delete_product')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product has deleted successfully')
    return redirect('catalog:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(status='PU')


class ProductDetailView(DetailView):
    """ Product detail page """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class HomeProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(status='PU')[:5]


class ContactsCreateView(LoginRequiredMixin, CreateView):
    """ Page for Contacts with Feedback message feature """
    model = FeedBackMessage
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:feedback_success')


class FeedBackMessageSent(TemplateView):
    template_name = 'catalog/feedback_success.html'


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:product_created')


class ProductCreated(TemplateView):
    template_name = 'catalog/product_created.html'
