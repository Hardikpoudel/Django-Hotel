from rest_framework import serializers
from room.models import roomType, room, roomReservation
from reservation_api.serializers import reservationSerializer
from Image.models import picture


class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = picture
        fields = '__all__'


class roomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = roomType
        fields = '__all__'


class roomSerializer(serializers.ModelSerializer):
    # typeID = roomTypeSerializer(read_only=False)
    pictureID = imageSerializer()

    class Meta:
        model = room
        fields = '__all__'

    # def create(self, validate_data):
    #     room_data = validate_data.pop('typeID')
    #     room


class roomReservationSerializer(serializers.ModelSerializer):
    roomID = roomSerializer()
    reservationID = reservationSerializer()

    class Meta:
        model = roomReservation
        fields = '__all__'
