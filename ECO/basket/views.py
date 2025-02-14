from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from store.models import Product
from .basket import Basket
from django.contrib.auth import get_user_model

User = get_user_model()


def basket_summary(request):
    basket = Basket(request)
    context = {'basket': basket}
    if not request.user.is_anonymous:
        user = User.objects.get(id=request.user.id)
        context["green_points"] = user.green_point

    return render(request, 'basket/summary.html',context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)

        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_greenpoint()
        subtotalprice = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal, 'subtotal-price': subtotalprice})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))

        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_greenpoint()

        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
