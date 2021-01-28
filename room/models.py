from django.db import models
from reservation.models import reservation
# Create your models here.


class roomType(models.Model):
    typeName = models.CharField(max_length=50)


class room(models.Model):
    typeID = models.ForeignKey(roomType, on_delete=models.CASCADE)
    roomName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    beds = models.IntegerField()
    price = models.IntegerField()


class roomReservation(models.Model):
    roomID = models.ForeignKey(room, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    totalPrice = models.IntegerField()
