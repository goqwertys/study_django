from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED



class ProductService:
    """Service class for .models.Product"""

    @staticmethod
    def get_products_from_cache():
        """ Returns product list from cache if it there. """
        if not CACHE_ENABLED:
            return Product.objects.filter(status='PU')
        key = 'products'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.filter(status='PU')
        cache.set(key, products)
        return products

    @staticmethod
    def filtered_by_category(category_id):
        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def get_category_name(category_id):
        category = Category.objects.get(id=category_id)
        return category.name
