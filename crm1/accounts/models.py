from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# IMPORTANT_NOTE - 1. Do makemigrations --> 2. Do migrate --> 3. Add it in admin.py

class Customer(models.Model):
    user            = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # One Customer can have only one User
    name            = models.CharField(max_length=200, null = True) # null = True -> if empty so that it doesn't show error
    phone           = models.CharField(max_length=200, null = True)
    email           = models.CharField(max_length=200, null = True)
    date_created    = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null = True) # null = True -> if empty so that it doesn't show error
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name        = models.CharField(max_length=200, null = True)
    price       = models.FloatField(null=True)
    category    = models.CharField(max_length=200, null= True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tags        = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending',     'pending'),
        ('Out of Stock','stock finish'),
        ('Delivered',   'delivered'),
    )

    customer    = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product     = models.ForeignKey(Product, null = True, on_delete= models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status      = models.CharField(max_length=200, null = True, choices=STATUS)
    note        = models.CharField(max_length=1000, null = True)

    
    def __str__(self):
        return self.product.name