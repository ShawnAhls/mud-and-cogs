def contents(request):

    basket_list = {}
    total = 0
    part_count = 0

    context = {
        'basket_list': basket_list,
        'part_count': part_count,
        'total': total,
    }

    return context
