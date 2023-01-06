from django.db import models

# Create your models here.


class Products(models.Model):
    pro_name=models.CharField(max_length=120,unique=True)
    price=models.PositiveIntegerField(default=50)
    description=models.CharField(max_length=100)


    def __str__(self):
        return self.pro_name


class Carts(models.Model):
    item=models.ForeignKey(Products,on_delete=models.CASCADE)
    