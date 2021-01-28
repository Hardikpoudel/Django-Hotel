from django.db import models

# Create your models here.


class mealType(models.Model):
    typenName = models.CharField(max_length=50)


class meal(models.Model):
    typeID = models.ForeignKey(mealType, on_delete=models.CASCADE)
    mealName = models.CharField(max_length=50)
    price = models.IntegerField()
