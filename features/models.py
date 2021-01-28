from django.db import models
from django.utils import timezone
# Create your models here.


class guest(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)


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


class event(models.Model):
    eventName = models.CharField(max_length=50)
    price = models.IntegerField()


class eventReservation(models.Model):
    eventID = models.ForeignKey(event, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    noOfGuest = models.IntegerField()
    totalPrice = models.IntegerField()
    purposeDescribe = models.CharField(max_length=500)


class diningHall(models.Model):
    hallName = models.CharField(max_length=50)
    tableNo = models.IntegerField()


class mealType(models.Model):
    typenName = models.CharField(max_length=50)


class meal(models.Model):
    typeID = models.ForeignKey(mealType, on_delete=models.CASCADE)
    mealName = models.CharField(max_length=50)
    price = models.IntegerField()


class diningHallReservation(models.Model):
    mealID = models.ForeignKey(meal, on_delete=models.CASCADE)
    hallID = models.ForeignKey(diningHall, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    totalPrice = models.IntegerField()


class guestInvoice(models.Model):
    reservationID = models.ForeignKey(reservation, on_delete=models.CASCADE)
    guestID = models.ForeignKey(guest, on_delete=models.CASCADE)
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
