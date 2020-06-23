from django.shortcuts import render, get_object_or_404
from .models import Parts, Categories
from django.db.models import Q


def parts(request):

    parts = Parts.objects.all()
    query = None
    categories = None

    if 'q' in request.GET:
        query = request.GET['q']
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        parts = parts.filter(queries)

    if 'category' in request.GET:
        categories = request.GET['category']
        parts = parts.filter(category__name__in=categories)
        categories = Categories.objects.filter(name__in=categories)

    context = {
        'parts': parts,
        'lookup': query,
        'current_category': categories,
    }

    return render(request, "parts/parts.html", context)


def part_detail(request, part_id):

    part = get_object_or_404(Parts, pk=part_id)

    context = {
        'part': part,
    }

    return render(request, "parts/part_detail.html", context)
