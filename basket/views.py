from django.shortcuts import render


def basket(request):
    return render(request, "basket/basket.html")


def add_to_basket(request, item_id):

    quanity = int(request.POST.get('quanity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quanity
    else:
        basket[item_id] = quanity

    request.session['basket'] = basket
    print(request.session['basket'])
    return render(request, "basket/basket.html")
