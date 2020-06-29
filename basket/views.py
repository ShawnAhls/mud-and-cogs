from django.shortcuts import render


def basket(request):
    return render(request, "basket/basket.html")


def add_to_basket(request, item_id):

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return render(request, "basket/basket.html")
