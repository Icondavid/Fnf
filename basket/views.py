from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .basket import Basket
from  fnfwebapp.models import Products
from django.http import JsonResponse

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'orderSummary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Products, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket._len_()
        response = JsonResponse({'qty': basketqty})
        return response
    

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response