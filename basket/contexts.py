from django.shortcuts import get_object_or_404
from parts.models import Parts
from decimal import Decimal
from django.conf import settings


def contents(request):

    basket_items = []
    part_count = 0
    total = 0
    basket = request.session.get('basket', {})

    if total < settings.FREE_POSTAGE_THRESHOLD:
        postage = total * Decimal(settings.STANDARD_POSTAGE_PERCENTAGE / 100)
        free_postage_delta = settings.FREE_POSTAGE_THRESHOLD - total
    else:
        postage = 0
        free_postage_delta = 0

    grand_total = postage + total

    context = {
        'basket_items': basket_items,
        'part_count': part_count,
        'total': total,
        'postage': postage,
        'free_postage_delta': free_postage_delta,
        'free_postage_threshold': settings.FREE_POSTAGE_THRESHOLD,
        'grand_total': grand_total,
    }

    for item_id, quantity in basket.items():
        part = get_object_or_404(Parts, pk=item_id)
        total += quantity * part.price
        part_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'part': part,
        })

    return context
