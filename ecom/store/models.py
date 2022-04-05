from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, max_length=100)
    name = models.CharField(null=True, max_length=50)
    email = models.EmailField(max_length=250, null=True )
  
    # to save the data
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(null=True, max_length=50)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems =self.orderItem_set.all()
        total = sum([item.get_total for item in orderItems])
        return total

    @property
    def get_cart_items(self):
        orderitems =self.orderItem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total 



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(null=True, max_length=50)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    zipcode = models.CharField(null=True, max_length=50)
    date_added  = models.CharField(null=True, max_length=50)

    def __str__(self):
        return str.address