from django.db import models
from product.models import Product

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    
    def __str__(self):
        return f'Cart {self.session_key}'
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.item.all())
    
    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.item.all())
    
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
        unique_together = ['cart', 'product']


    def __str__(self):
        return f'{self.quantity} x {self.product.title}'
    
    @property
    def total_price(self):
        return self.quantity * self.product.price
    




