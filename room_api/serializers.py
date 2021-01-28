from rest_framework import serializers
from room.models import roomType, room, roomReservation


class roomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = roomType
        fields = '__all__'


class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = '__all__'


class roomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = roomReservation
        fields = '__all__'
