from django.contrib import admin

from .models import Directory, Categories, Products


admin.site.register(Directory)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.empty_value_display = 'Не задано'
