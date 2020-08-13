from django.shortcuts import render, get_object_or_404
from .models import Parts, Category
from django.db.models import Q


def parts(request):

    parts = Parts.objects.all()
    category = None
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            parts = parts.filter(queries)

        if 'category' in request.GET:
            category = request.GET['category']
            parts = parts.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

    context = {
        'parts': parts,
        'lookup': query,
        'category': category,
    }

    return render(request, "parts/parts.html", context)


def part_detail(request, part_id):

    part = get_object_or_404(Parts, pk=part_id)

    context = {
        'part': part,
    }

    return render(request, "parts/part_detail.html", context)
