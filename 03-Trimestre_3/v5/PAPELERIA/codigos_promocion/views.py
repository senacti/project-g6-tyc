from django.shortcuts import render

from django.http import JsonResponse

from .models import PromoCode

from carts.utils import get_or_create_cart
from pedidos.utils import get_or_create_order

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def validate(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    code = request.GET.get('code')
    promo_code = PromoCode.objects.get_valid(code)

    if promo_code is None:
        return JsonResponse({
            'status': False
        }, status=404)

    order.apply_promo_code(promo_code)

    return JsonResponse({
        'status': True, 
        'code': promo_code.code,
        'discount': promo_code.discount,
        'total': order.total
    })

class PromoCodeListView(ListView):
    model = PromoCode
    template_name = 'web_cerrada/promo_codes/lista_promociones.html'
    context_object_name = 'promociones'

class PromoCodeCreateView(CreateView):
    model = PromoCode
    fields = ['code', 'discount', 'valid_from', 'valid_to']
    template_name = 'web_cerrada/promo_codes/crear_promocion.html'
    success_url = reverse_lazy('promo_codes:lista_promociones')

class PromoCodeUpdateView(UpdateView):
    model = PromoCode
    fields = ['code', 'discount', 'valid_from', 'valid_to']
    template_name = 'web_cerrada/promo_codes/actualizar_promocion.html'
    success_url = reverse_lazy('promo_codes:lista_promociones')

class PromoCodeDeleteView(DeleteView):
    model = PromoCode
    template_name = 'web_cerrada/promo_codes/eliminar_promocion.html'
    success_url = reverse_lazy('promo_codes:lista_promociones')
