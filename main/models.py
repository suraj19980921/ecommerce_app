from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.shop_name

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_name = models.CharField(max_length=250, null=False, blank=False)
    item_image = models.ImageField(blank=True, null=True)
    item_price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    item_description = models.TextField(null=False, blank=False )
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total_amount = models.FloatField()

    def __str__(self):
        return self.item_id.item_name

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE, related_name="order_item")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name="shop_item")
    purchase_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    shipping_address = models.TextField(max_length=500)
    pincode = models.IntegerField()
    mobile_no = models.IntegerField()
    
    def __str__(self):
        return self.item_id.item_name
    
    

