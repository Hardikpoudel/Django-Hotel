from rest_framework import serializers
from event.models import event, eventReservation


class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'


class eventReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventReservation
        fields = '__all__'
