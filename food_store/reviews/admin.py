from django.contrib import admin

from .models import Directory, Categories, Products, Cart, CartItem


admin.site.register(Directory)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.empty_value_display = 'Не задано'
