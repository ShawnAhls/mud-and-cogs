from django.shortcuts import render, get_object_or_404
from .models import Parts
from django.db.models import Q


def parts(request):

    parts = Parts.object.all()

    if 'q' in request.GET:
        query = request.GET['Q']
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        parts = parts.filter(queries)

    context = {
        'parts': parts,
        'lookup': query,
    }

    return render(request, "parts/parts.html", context)


def part_detail(request, part_id):

    part = get_object_or_404(Parts, pk=part_id)

    context = {
        'part': part,
    }

    return render(request, "parts/part_detail.html", context)
