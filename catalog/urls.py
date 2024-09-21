from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import home, contacts, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', product_list, name='products')
]
