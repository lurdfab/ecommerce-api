from django.db import models

DELIVERY = (
    ("free", "free"),
    ("standard", "standard"),
    ("express", "express")
)

class Order(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    delivery = models.CharField(choices=DELIVERY, default="free")
    coupon = models.ForeignKey("discount.Discount", on_delete=models.SET_NULL, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)  #I need to implement the order status after created and payment is made
    
    
    def __str__(self):
        return f"Order for {self.user.username}"
    

    def get_total_amount(self):
        data = OrderItem.objects.filter(order=self)
        total = 0
        for order in data:
            total += order.quantity * order.product.price

        return total
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order for {self.order.user.username}"