from tkinter.font import names

from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, HomeProductListView, ProductDetailView, \
    ContactsCreateView, FeedBackMessageSent, AddProduct, ProductCreated, unpublish_product, delete_product, \
    ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeProductListView.as_view(), name='home'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('contacts/success/', FeedBackMessageSent.as_view(), name='feedback_success'),
    path('add_product/', AddProduct.as_view(), name='add_product'),
    path('product_created/', ProductCreated.as_view(), name='product_created'),
    path('products/<int:pk>/unpublish', unpublish_product, name='unpublish_product'),
    path('products/<int:pk>/delete', delete_product, name='delete_product'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='edit_product'),
]
