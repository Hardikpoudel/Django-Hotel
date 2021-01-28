from django.db import models
from django.utils import timezone
# Create your models here.


class guest(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
