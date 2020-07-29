from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PurchaseForm
from basket.contexts import contents
from django.conf import settings

import stripe


def purchase(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request,
                       "Your have an empty basket")
        return redirect(reverse('parts'))

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_basket = contents(request)
    total = current_basket['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    print(intent)

    purchase_form = PurchaseForm()
    template = 'purchase/purchase.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
