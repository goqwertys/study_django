from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED



class ProductService:
    """Service class for .models.Product"""

    @staticmethod
    def get_products_from_cache():
        if not CACHE_ENABLED:
            return Product.objects.filter(status='PU')
        key = 'products'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.filter(status='PU')
        cache.set(key, products)
        return products
