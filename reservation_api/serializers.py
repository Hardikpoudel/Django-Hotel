from rest_framework import serializers
from reservation.models import reservation
from guest_api.serializers import guestSerializer


class reservationSerializer(serializers.ModelSerializer):
    guestID = guestSerializer()

    class Meta:
        model = reservation
        fields = '__all__'
