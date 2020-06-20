from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Products


def products(request):

    products = Products.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
         'products': products,
         'search_term': query,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):

    product = get_object_or_404(Products, pk=product_id)

    context = {
         'product': product,
    }

    return render(request, "products/product_details.html", context)
