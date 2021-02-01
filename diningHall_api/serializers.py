from rest_framework import serializers
from diningHall.models import diningHall, diningHallReservation
from meal_api.serializers import mealSerializer
from reservation_api.serializers import reservationSerializer


class hallSerializer(serializers.ModelSerializer):
    class Meta:
        model = diningHall
        fields = '__all__'


class hallReservationSerializer(serializers.ModelSerializer):
    mealID = mealSerializer()
    hallID = hallSerializer()
    reservationID = reservationSerializer()

    class Meta:
        model = diningHallReservation
        fields = '__all__'
