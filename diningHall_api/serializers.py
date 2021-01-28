from rest_framework import serializers
from diningHall.models import diningHall, diningHallReservation


class hallSerializer(serializers.ModelSerializer):
    class Meta:
        model = diningHall
        fields = '__all__'


class hallReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = diningHallReservation
        fields = '__all__'
