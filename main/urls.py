from django.template.defaulttags import csrf_token
from django.urls import path
from .views import get_products, get_detail, add_product

app_name = 'main'  # => main:index

urlpatterns = [
    path('', get_products, name='index'),
    path('add-product', add_product, name='add-product'),
    path('product-details<int:product_id>', get_detail, name='product-detail'),
]
