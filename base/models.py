from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    worker = models.BooleanField(default=False)
    fullName = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=12,unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fullName},{self.phoneNumber},{self.address}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=30)
    productDescription = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.productName},{self.price}"

class Order(models.Model):
    client =models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    id = models.AutoField(primary_key=True)
    orderDate = models.DateField(null=True)
    orderTime = models.TimeField(null=True)
    orderStatus = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)
    orderType = models.BooleanField(default=False)
    total = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id},{self.client},{self.total},{self.orderDate},{self.orderTime},{self.orderStatus}"
    

class OrderDetails(models.Model):
    product =models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order =models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"{self.order},{self.quantity},{self.total}"

class TodayAmount(models.Model):
    id = models.AutoField(primary_key=True)
    todayDate = models.DateField(null=True)
    startAmount = models.IntegerField(null=True)
    totalInDelivary = models.IntegerField(null=True)
    totalInPickup = models.IntegerField(null=True)
    leftAmount = models.IntegerField(null=True)
    totalPrice = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.todayDate},{self.startAmount}"
        
    