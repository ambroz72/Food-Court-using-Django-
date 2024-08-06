from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pydoc import describe

# Create your models here.
class Category(models.Model):       #admin....
    product_category = models.CharField(max_length=100,null=True)
    product_price = models.IntegerField(null=True)
    product_stock = models.IntegerField(null=True)
    
class User(models.Model):       #user....
    e_category =models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    e_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    e_fname = models.CharField(max_length=30,null=True)
    e_lname = models.CharField(max_length=30,null=True)
    e_address = models.CharField(max_length=100,null=True)
    e_phone_numbr = models.BigIntegerField(10,null=True)
    e_email = models.EmailField(null=True)

class Product(models.Model):
    p_category =models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    p_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=30,null=True)
    product_desc = models.TextField(max_length=100,null=True)
    product_price = models.IntegerField(null=True)
    product_img = models.ImageField(upload_to='img/',null=True)
    product_qty =models.IntegerField(null=True)
    
class Feedback(models.Model): 
    f_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    f_name=models.CharField(max_length=50,null=True)
    f_feed=models.CharField(max_length=100,null=True)
    f_DOB=models.DateField(null=True)
    f_status=models.CharField(max_length=30,null=True)
    
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True,null=True)
    date_added=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        db_table='Cart'
        ordering=['date_added']
        
    def __str__(self):
        return '{}'.format (self.cart_id)
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    active=models.BooleanField(default=True,null=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return '{}'.format (self.product)
    
    

