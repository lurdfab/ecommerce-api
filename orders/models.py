from django.db import models



class Order(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(max_length=100)
    is_delivered = models.BooleanField(default=False)
    
    
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