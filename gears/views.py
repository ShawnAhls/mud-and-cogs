from django.shortcuts import render, get_object_or_404
from .models import Gears


def gears(request):

    gears = Gears.objects.all()

    context = {
        'gears': gears,
    }

    return render(request, "gears/gears.html", context)


def gear_detail(request, product_id):

    gear = get_object_or_404(gears, pk=product_id)

    context = {
         'gear': gear,
    }

    return render(request, "gears/gear_detail.html", context)
