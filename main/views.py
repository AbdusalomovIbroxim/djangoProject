from django.shortcuts import render, redirect
from django.views import View

from products.forms import ProductModelForm
from products.models import Product


def get_products(request):
    products = Product.objects.all()
    return render(request, "app/index.html", {"products": products})


class IndexView(View):
    pass


def get_detail(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    return render(request, "app/product_detail.html", {"product": product})


class Product_detail(View):
    pass


def add_product(request):
    form = ProductModelForm()

    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main:index')

    context = {
        "form": form
    }
    return render(request, "app/add-product.html", context)


class AddProduct(View):
    pass
