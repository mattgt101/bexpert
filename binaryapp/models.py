from django.db import models
import datetime
from cloudinary.models import CloudinaryField


# Create your models here.

class Member(models.Model):
     fname = models.CharField(max_length=200, blank=True, null=True)
     lname = models.CharField(max_length=200, blank=True, null=True)
     email = models.CharField(max_length=200, primary_key=True)
     phone = models.CharField(max_length=200, blank=True, null=True)
     country = models.CharField(max_length=200, blank=True, null=True)
     pword = models.CharField(max_length=200, blank=True, null=True)
     code = models.CharField(max_length=200, blank=True, null=True)

     invest = models.FloatField(blank=True,null=True,default=0.0)
     profit = models.FloatField(blank=True,null=True,default=0.0)
     bonus = models.FloatField(blank=True,null=True,default=0.0)
     bal = models.FloatField(blank=True,null=True,default=0.0)
     btc_equ = models.CharField(max_length=200, blank=True, null=True, default='0.0000000')

     id_type= models.CharField(max_length=200, blank=True, null=True)
     id_front = CloudinaryField('id_front', null=True, blank=True)
     id_back = CloudinaryField('id_back', null=True, blank=True)

     def __str__(self):
         return self.fname +' '+ self.lname

class History(models.Model):
    amount = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, default='pending')
    email= models.CharField(max_length=100, blank=True, null=True)
    wallet = models.CharField(max_length=100,default='self', blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())

    def __str__(self):
         return self.email

class Manage(models.Model):
    site = models.CharField(default='site', max_length=200,primary_key=True)
    btc_wallet = models.CharField(max_length=2000, blank=True, null=True)
    eth_wallet = models.CharField(max_length=2000, blank=True, null=True)
    phone = models.CharField(max_length=2000, blank=True, null=True)
    email = models.CharField(max_length=2000, blank=True, null=True)
    add = models.CharField(max_length=2000, blank=True, null=True)
    admin = models.CharField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return self.site