from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem
from product.models import Product
from django.contrib import messages
from django.views.decorators.http import require_POST


def _get_cart(request):
    if not request.session.session_key:
        request.session.create()
    
    cart, created = Cart.objects.get_or_create(session_key = request.session.session_key)
    return cart



def cart_detail(request):
    cart = _get_cart(request)
    context = {
        'cart':cart
    }
    return render(request, 'cart/detail.html', context)

@require_POST
def cart_add(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity':1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Кол-во товара {product.title} увеличено")
    else:
        messages.success(request, f"Товар {product.title} добавлен")

    return redirect("product:home")


@require_POST
def cart_remove(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    try:
        cart_item, created = CartItem.objects.get(
            cart=cart,
            product=product
        )
        cart_item.delete()
        messages.success(request, f"Товар {product.title} удален")
    except CartItem.DoesNotExist:
        messages.error(request, f"Товар не найден в корзине")


    return redirect("cart:cart_detail")


@require_POST
def cart_update(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity',1))
    
    try:
        cart_item = CartItem.objects.get(
            cart=cart,
            product=product
        )
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f"Кол-во товара {product.title} изменено")
        else:
            cart_item.delete()
            messages.success(request, f"Товар {product.title} удален из корзины")

    except CartItem.DoesNotExist:
            messages.error(request, f"Товар не найден в корзине")
    
   

    return redirect("cart:cart_detail")