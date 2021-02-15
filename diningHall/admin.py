from django.contrib import admin
from room.models import room, roomType, roomReservation
from reservation.models import reservation
from guest.models import guest
# Register your models here.

admin.site.register(room)
admin.site.register(roomType)
admin.site.register(reservation)
admin.site.register(guest)
admin.site.register(roomReservation)
