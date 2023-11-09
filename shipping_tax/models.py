from django.db import models

DELIVERY = (
    ("free", "free"),
    ("standard", "standard"),
    ("express", "express")
)

AMOUNT = (
    (0, 0),
    (10, 10),
    (20, 20)
)

class Shipping(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    town = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=50)
    delivery = models.CharField(choices=DELIVERY, default="free")
    amount = models.CharField(choices=DELIVERY, default=0)

    def __str__(self):
        return self.name
    
    

# class Tax(models.Model):
#     name = models.CharField(max_length=255)
#     rate = models.DecimalField(max_digits=5, decimal_places=2)
#     location = models.CharField(max_length=255, blank=True, null=True)
#     product_category = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.name