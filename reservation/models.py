from django.db import models
from django.utils import timezone
from guest.models import guest
# Create your models here.


class reservation(models.Model):
    guestID = models.ForeignKey(guest, on_delete=models.CASCADE)
    checkIn = models.DateTimeField()
    checkOut = models.DateTimeField()
    # timestamp when the reservation was created or updated
    tsCreated = models.DateTimeField(editable=False)
    tsUpdated = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps 
        created is only updated if id is not set
        i.e. item is first created
        '''
        if not self.id:
            self.tsCreated = timezone.now()
        self.tsUpdated = timezone.now()
        return super(reservation, self).save(*args, **kwargs)


class reserved(models.Model):
    status = models.BooleanField(default=False)
