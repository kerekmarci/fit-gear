from django.db import models
from store.models import Product


class Bag(models.Model):
    bag_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class BagItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product