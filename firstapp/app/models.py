from datetime import time
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager


# Create your models here.

    
class room(models.Model,):
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
class UserManager(BaseUserManager):
    def create_user(self, firstName, lastName, email, password=None):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        if not firstName:
            raise ValueError("First Name is required")
        if not lastName:
            raise ValueError("Last Name is required")
        
        
        user = self.model(
            firstName=firstName,
            lastName=lastName,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,firstName,lastName,email,password=None):
        user = self.create_user(firstName,lastName,email,password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin=True
        user.save(using=self._db)
        
        return user
    
class All_Users(AbstractBaseUser):
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    email    = models.EmailField(max_length=120, null=False,unique=True)
    password = models.CharField(max_length=255, null=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    objects = UserManager()

    class Meta:
        verbose_name_plural = "All Users"
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

