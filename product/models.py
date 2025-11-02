from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# python manage.py makemigrations
# python manage.py migrate


class Product(models.Model):
    title =  models.CharField(max_length=200, verbose_name="Название товара")
    short_description =  models.CharField(max_length=200, verbose_name="")
    description =  models.TextField()
    price = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_compleated = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.username