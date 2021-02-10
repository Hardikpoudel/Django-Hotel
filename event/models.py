from django.db import models
from reservation.models import reservation, reserved
# Create your models here.


class event(models.Model):
    eventName = models.CharField(max_length=50)
    price = models.IntegerField()


class eventReservation(models.Model):
    eventID = models.ForeignKey(event, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    reservedID = models.ForeignKey(reserved, on_delete=models.CASCADE)
    noOfGuest = models.IntegerField()
    totalPrice = models.IntegerField()
    purposeDescribe = models.CharField(max_length=500)
