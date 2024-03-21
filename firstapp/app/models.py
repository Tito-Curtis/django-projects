from datetime import time
from django.db import models

# Create your models here.

    
class room(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    floor_room = models.IntegerField()
    

    def __str__(self):
        return f'{self.name} - {self.room_number}'
    
class meetings(models.Model):
    title = models.CharField(max_length=100)
    date  = models.DateField()
    time  = models.TimeField()
    duration = models.IntegerField()
    room     = models.ForeignKey(room,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Meetings"
    def __str__(self):
        return f'{self.title} - {self.time}'
    

class Product(models.Model):
    name= models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price       = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self): #
        return self.name

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)
class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product')

    class Meta:
        verbose_name_plural = "Categories"   #p

    def __str__(self):
        return self.name

class All_Users(models.Model):
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    email    = models.EmailField(max_length=120, null=False)
    password = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name_plural = "All Users"
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

