from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    is_teamleader = models.BooleanField('Is teamleader', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    empimage=models.ImageField(upload_to="image")
    is_active=models.BooleanField(default=True,verbose_name="Available")

class Employee(models.Model):
    name=models.CharField(max_length=50,verbose_name="Employee Name")
    employeeid=models.BigIntegerField()
    gender=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100,verbose_name="Address")
    salary=models.FloatField()
    performance=models.CharField(max_length=50, verbose_name="Emp Performance")
    doj=models.DateField()
    empimage=models.ImageField(upload_to="image")
    is_active=models.BooleanField(default=True,verbose_name="Available")

class Teamleader(models.Model):
    name=models.CharField(max_length=50,verbose_name="Employee Name")
    employeeid=models.BigIntegerField()
    gender=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100,verbose_name="Address")
    salary=models.FloatField()
    performance=models.CharField(max_length=50, verbose_name="Emp Performance")
    doj=models.DateField()
    empimage=models.ImageField(upload_to="image")
    is_active=models.BooleanField(default=True,verbose_name="Available")

class Manager(models.Model):
    name=models.CharField(max_length=50,verbose_name="Employee Name")
    employeeid=models.BigIntegerField()
    gender=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=100,verbose_name="Address")
    salary=models.FloatField()
    performance=models.CharField(max_length=50, verbose_name="Emp Performance")
    doj=models.DateField()
    empimage=models.ImageField(upload_to="image")
    is_active=models.BooleanField(default=True,verbose_name="Available")