from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import PurchaseForm
from basket.contexts import contents
from django.conf import settings
from parts.models import Parts
from .models import Purchase, PurchasePart

import stripe
import json


def purchase(request):
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        purchase_form = PurchaseForm(form_data)
        if purchase_form.is_valid():
            purchase = purchase_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            purchase.stripe_pid = pid
            purchase.original_basket = json.dumps(basket)
            purchase.save()
            for item_id, item_data in basket.items():
                try:
                    parts = Parts.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        purchase_line_item = PurchasePart(
                            purchase=purchase,
                            parts=parts,
                            quantity=item_data,
                        )
                        purchase_line_item.save()
                except Parts.DoesNotExist:
                    messages.error(request, (
                        "A part in your basket can not be "
                        "found in our database. "
                        "Please contact our Customer Helpline")
                    )
                    purchase.delete()
            return render(reverse('purchase',
                                  args=[purchase.purchase_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please ensure your information'
                                     'is correct.'))
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your have an empty basket")
        return redirect(reverse('purchase'))

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

    purchase_form = PurchaseForm()
    template = 'purchase/purchase.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def purchase_successful(request, purchase_number):
    purchase = get_object_or_404(Purchase, purchase_number=purchase_number)
    messages.success(request, f'Your purchase was successfully processed! \
        Your purchase number is {purchase_number}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'purchase/purchase_successful.html'
    context = {
        'purchase': purchase,
    }

    return render(request, template, context)
