# from django.conf import settings


def contents(request):

    basket_item = {}
    part_count = 0
    total = 0

    context = {
        'basket_item': basket_item,
        'part_count': part_count,
        'total': total,
    }

    return context
