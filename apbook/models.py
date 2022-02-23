
from atexit import register
import datetime
from email.headerregistry import Address
from email.policy import default
from django.db import models
from tables import Description



# Create your models here.
class clnt_info(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    emails=models.EmailField()
    password=models.CharField(max_length=255)
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.emails

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __self__(self):
        return self.name



class product(models.Model):
    productname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='upload/productimg')
    price=models.IntegerField(default=100)
    Description=models.CharField(max_length=255, default=100)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.productname


class order(models.Model):
    product=models.ForeignKey(product, on_delete=models.CASCADE)
    customer= models.ForeignKey(clnt_info,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    price=models.IntegerField()
    Address=models.CharField(max_length=50,default="",blank=True)
    phoneno=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self): 
        return self.Address
