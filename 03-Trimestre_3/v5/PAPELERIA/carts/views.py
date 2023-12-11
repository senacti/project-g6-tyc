from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import CartProductos
from productos.models import Producto

from .models import Cart
from .utils import get_or_create_cart

# Create your views here.
def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
        'cart':cart
    })
def add(request):
    cart = get_or_create_cart(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))
    quantity = int(request.POST.get('quantity', 1))

    #cart.productos.add(producto, through_defaults={
    #    'quantity': quantity
    #})

    cart_producto = CartProductos.objects.create_or_update_quantity(cart=cart, 
                                                                    producto=producto, 
                                                                    quantity=quantity)

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'cart_producto': cart_producto,
        'producto': producto
    })

def remove(request):
    cart = get_or_create_cart(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))

    cart.productos.remove(producto)

    return redirect('carts:cart')