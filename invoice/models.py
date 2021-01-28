from django.db import models

from reservation.models import reservation
from guest.models import guest
# Create your models here.


class invoice(models.Model):

    guestID = models.ForeignKey(guest, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    invoiceAmount = models.IntegerField()
    tsIssued = models.DateTimeField(editable=False)
    tsPaid = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps
        created is only updated if id is not set
        i.e. item is first created
        '''
        if not self.id:
            self.tsIssued = timezone.now()
        self.tsPaid = timezone.now()
        return super(guestInvoice, self).save(*args, **kwargs)
