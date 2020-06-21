from django.shortcuts import render, get_object_or_404
from .models import Gears
from django.db.models import Q


def gears(request):

    gears = Gears.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        gears = gears.filter(queries)

    context = {
        'gears': gears,
        'search_term': query,
    }

    return render(request, "gears/gears.html", context)


def gear_detail(request, gear_id):

    gear = get_object_or_404(Gears, pk=gear_id)

    context = {
        'gear': gear,
    }

    return render(request, "gears/gear_detail.html", context)
