from django.shortcuts import render, get_object_or_404
from .models import Products


def products(request, products_id):

    products = get_object_or_404(Products, pk=products_id)

    context = {
        'products': products,
    }

    return render(request, "products/products.html", context)
