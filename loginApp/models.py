from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from decimal import Decimal
# Create your models here.




class CustomerSignUp(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=100, blank=False)
   
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    address = models.CharField(
        max_length=250,  blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pic', )
    designation = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


# class CustomerLogin(models.Model):
#     username = models.CharField(max_length=250, blank=False, null=False)
#     password = models.PasswordField(max_length=100, blank=False)
