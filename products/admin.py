from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name", "price", "stock")

# class ProductVariantAdmin(admin.ModelAdmin):
    # list_display = ("id","product", "sizes", "colors")

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)

