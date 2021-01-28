from django.db import models
from reservation.models import reservation
from meal.models import meal
# Create your models here.


class diningHall(models.Model):
    hallName = models.CharField(max_length=50)
    tableNo = models.IntegerField()


class diningHallReservation(models.Model):
    mealID = models.ForeignKey(meal, on_delete=models.CASCADE)
    hallID = models.ForeignKey(diningHall, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    totalPrice = models.IntegerField()
