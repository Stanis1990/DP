from django.shortcuts import render
from product.models import Product, OrderItem

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
        }
    return render(request, 'product/home.html', context)



def order(request):
    orders = OrderItem.objects.filter(order__user = request.user)
    context = {
        'orders': orders
        }
    return render(request, 'product/order.html', context)