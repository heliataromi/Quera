from django.db.models import Sum
from django.http import Http404
import json

from .models import OrderItem

def checkout(request, order_pk):
    order = OrderItem.objects.filter(order=order_pk)
    if order is None:
        return Http404
    data = OrderItem.objects.filter(order=order_pk).aggregate(total_price=Sum('product__price'))
    data['total_price'] = round(data['total_price'], 2)
    return json.dumps(data)
