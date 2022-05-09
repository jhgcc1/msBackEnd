
from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    Client = models.CharField(max_length=255)
    Product = models.CharField(max_length=255)
    Price = models.FloatField()
    Quantity = models.FloatField(null=True,default=None,blank=True)


    
