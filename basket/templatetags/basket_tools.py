from django import template


register = template.Library()


@register.filter(name='add_subtotal')
def add_subtotal(price, quantity):
    return price * quantity
