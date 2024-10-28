from keyword import kwlist

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.contrib import messages
from django.utils.decorators import method_decorator
from unicodedata import category

from catalog.forms import ProductForm
from catalog.models import Product, FeedBackMessage
from catalog.services import ProductService


@permission_required('catalog.can_unpublish_product')
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.status = 'DR'
    product.save()
    messages.success(request, 'Product has unpublished successfully')
    return redirect('catalog:product_list')


@permission_required('catalog.delete_product')
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
        return ProductService.get_products_from_cache().filter(status='PU')


class CategoryProduct(ListView):
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.kwargs['category_id']

        context['products'] = ProductService.filtered_by_category(category_id)
        context['category_name'] = ProductService.get_category_name(category_id)
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    """ Product detail page """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/edit_product.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class ProductCreated(TemplateView):
    template_name = 'catalog/product_created.html'
