from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseForm


def purchase(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request,
                       "Your have an empty basket")
        return redirect(reverse('parts'))

    purchase_form = PurchaseForm()
    template = 'purchase/purchase.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': 'pk_test_51H7RYPI3nLn57BKyVjCEQsZMcFUK9Z0bADPxPi4pga5DEe38uagPRTi5pPl2rrHkTQ1ndgyjtJvOBwmHe61gKm4b001MN6iDcG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
