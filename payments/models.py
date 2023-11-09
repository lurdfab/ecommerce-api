from django.db import models
from paypalrestsdk import Payment
from orders.models import OrderItem
from django.shortcuts import resolve_url

STATUS = (
    ("pending", "pending"),
    ("successful", "successful"),
    ("declined", "declined")
)

PAYMENT_TYPE = (
    ("cash", "cash on delivery"),
    ("paypal", "paypal"),
    ("cc", "credit card"),
    ("transfer", "Bank Transfer")

)


class Payment(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default="pending")
    payment_type = models.CharField(choices=PAYMENT_TYPE, default="cash")
    description = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} - {self.order.get_total_amount()} - {self.timestamp}"

    def save(self, *args, **kwargs):
      
        super().save(*args, **kwargs) #how to use the customized save parameters for models
        

    def create_payment(self):
        data = OrderItem.objects.filter(order=self.order)
        items = dict()
        for order in data:
            items.append( {
                "name": order.product.name,
                "price": order.product.price,
                "currency": "USD",
                "quantity": order.quantity
            })
           
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": resolve_url("payment-paypal-success", {"id":self.order.id, "pk":self.id}),
                "cancel_url": resolve_url("payment-paypal-cancel", {"id":self.order.id, "pk":self.id})
            },
            "transactions": [
                {
                    "item_list": {
                        "items": items
                    },
                    "amount": {
                        "total": self.order.get_total_amount(),
                        "currency": "USD"
                    },
                    "description": "Description of the product"
                }
            ]
        })

        if payment.create():
            # Redirect the user to PayPal for payment
            for link in payment.links:
                if link.method == "REDIRECT":
                    return link.href
        else:
            # Handle payment creation error
            return None
        

#we need to implement a payment gateway for credit / debit cards next

