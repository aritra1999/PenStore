from django.db import models
from django.contrib.auth.models import User
    
from accounts.models import Customer
from ecommerce.utils import slug_generator

class Product(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='image', blank=True, null=True)
    color = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slug_generator(self.name, self.brand)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.transaction_id)
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.order)
    

