from django.http.response import JsonResponse
from django.shortcuts import render

from basket.basket import Basket

from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_greenpoint()
        context = {}
        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            context["success"] = "order exists"
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                         address2='add2', total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], greenpoint=item['greenpoint'],
                                         quantity=item['qty'])
            order.billing_status = True
            order.save()
            context["success"] = "order does not exists"

        return JsonResponse(context)


# def payment_confirmation(data):
#     # Order.objects.filter(order_key=data).update(billing_status=True)
#     order = Order.objects.filter(order_key=data)
#     order.billing_status = True
#     order.save()


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
