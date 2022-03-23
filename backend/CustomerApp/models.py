from django.db import models


# Create your models here.

class Customers(models.Model):
    customerID = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=200)
    customerPhone = models.IntegerField()
    customerAddress = models.CharField(max_length=300)


class Mechanic(models.Model):
    mechanicID = models.AutoField(primary_key=True)
    mechanicName = models.CharField(max_length=200)
    mechanicAddress = models.CharField(max_length=200)
    mechanicPhone = models.IntegerField()
