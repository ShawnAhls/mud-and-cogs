from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .form import PurchaseForm


def purchase(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request,
                       "Your have an empty basket")
        return redirect(reverse('parts'))

    purchase_form = PurchaseForm()
    template = "purchase/purchase.html"
    context = {
        'purchase_form': purchase_form,
    }

    return render(request, template, context)
