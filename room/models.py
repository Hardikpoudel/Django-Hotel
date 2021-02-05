from django.db import models
from reservation.models import reservation
from Image.models import picture
from django.utils.text import slugify
# Create your models here.


class roomType(models.Model):
    typeName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.typeName

class room(models.Model):
    typeID = models.ForeignKey(roomType, on_delete=models.CASCADE)
    pictureID = models.ForeignKey(picture, on_delete=models.CASCADE)
    roomSlug = models.SlugField(max_length=250, blank=True)
    roomName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    beds = models.IntegerField()
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.roomSlug:
            t_slug = slugify(self.beds)
            origin = 1
            unique_slug = t_slug
            while room.objects.filter(roomSlug=unique_slug).exists():
                unique_slug = '{}{}'.format(t_slug, origin)
                origin += 1
            self.roomSlug = unique_slug
        super().save(*args, **kwargs)


class roomReservation(models.Model):
    roomID = models.ForeignKey(room, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    totalPrice = models.IntegerField()
