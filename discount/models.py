from django.db import models

CATEGORY = (
    ("percentage", "percentage"),
    ("cash", "cash")
)
    


class Discount(models.Model):
    coupon = models.CharField(max_length=255, unique=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(choices=CATEGORY, default="cash")

    def __str__(self):
        return self.coupon