# from django.conf import settings


def contents(request):

    basket_item = {}
    total = 0
    part_count = 0

    context = {
        'basket_item': basket_item,
        'part_count': part_count,
        'total': total,
    }

    return context
