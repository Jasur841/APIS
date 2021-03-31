from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel,TreeForeignKey
from location_field.models.plain import PlainLocationField


class Client(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    balance = models.IntegerField(default=0,null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    location = models.CharField(max_length=100)



    def __str__(self):
        return self.username



class Category(MPTTModel):

    parent = TreeForeignKey('self', on_delete=models.CASCADE,blank=True,null=True,related_name='children')
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='image', null=True)
    slug = models.SlugField(max_length=50)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    quantity = models.IntegerField()
    old_price = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    bank = models.CharField(max_length=25)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    is_success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now=True, null=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

