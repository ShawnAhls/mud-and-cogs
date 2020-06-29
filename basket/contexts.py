from django.shortcuts import get_object_or_404
from parts.models import Parts


def contents(request):

    basket_items = []
    part_count = 0
    total = 0
    basket = request.session.get('basket', {})

    context = {
        'basket_items': basket_items,
        'part_count': part_count,
        'total': total,
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
