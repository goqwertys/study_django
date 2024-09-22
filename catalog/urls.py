from tkinter.font import names

from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import home, contacts, product_list, product_detail, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', product_list, name='products'),
    path('products/<int:pk>', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
]
