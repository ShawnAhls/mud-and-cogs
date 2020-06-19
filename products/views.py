from django.shortcuts import render, get_object_or_404
from .models import Products


def products(request):

    products = Products.objects.all()

    context = {
         'products': products,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):

    product = get_object_or_404(Products, pk=product_id)

    context = {
         'product': product,
    }

    return render(request, "products/product_details.html", context)
