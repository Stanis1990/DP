from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from product.models import Product, Order, OrderItem, CustomUser

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'availability', 'created_at')
    list_filter = ('availability', 'created_at')
    search_fields = ('title', 'price',)
    list_editable = ('price', 'availability')

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','created_at', 'is_compleated')
    list_filter = ('is_compleated', 'created_at')
    inlines = [OrderItemAdmin]

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                "avatar", "phone"
            ),
        }),
    )
    