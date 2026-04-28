from django import template

register = template.Library()

@register.filter
def format_price(value):
    if value:
        return f'{int(value):,}'.replace(',', ' ')
    return '0'

@register.filter
def discount(product, old_price):
    if old_price and old_price > 0:
        return int(((old_price - product.price) / old_price) * 100)
    return 0