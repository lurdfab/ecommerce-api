from django.db import models

COLORS = (
    (0, "Red"),
    (1, "Blue"),
    (2, "White"),
    (3, "Black"),
    (4, "Grey"),
    (5, "Green"),
    (6, "Matte")
)

RATING = (
    (0, ""),
    (1, "1 star"),
    (2, "2 stars"),
    (3, "3 stars"),
    (4, "4 stars"),
    (5, "5 stars"),
)



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# class SizeVariant(models.Model):
#     product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='sizevariant')
#     size = models.CharField(max_length=50)

# class ColorVariant(models.Model):
#     product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='colorvariant')
#     colors = models.CharField(choices=COLORS, max_length=50) 


# class VariantManager(models.Manager):
#     def sizes(self):
#         # print(self)
#         return SizeVariant.objects.filter(product=self)
    
    
#     def colors(self):
#         return ColorVariant.objects.filter(product=self)


class Product(models.Model):
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # objects = models.Manager()
    # variants = VariantManager()


    def __str__(self):
        return self.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING, default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'owner')




    


    



