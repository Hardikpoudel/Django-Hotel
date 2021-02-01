from rest_framework import serializers
from event.models import event, eventReservation
from reservation_api.serializers import reservationSerializer


class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'


class eventReservationSerializer(serializers.ModelSerializer):
    eventID = eventSerializer()
    reservationID = reservationSerializer()

    class Meta:
        model = eventReservation
        fields = '__all__'
