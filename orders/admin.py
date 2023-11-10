from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "order_date", "is_delivered")

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
