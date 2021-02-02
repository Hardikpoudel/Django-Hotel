from rest_framework import serializers
from room.models import roomType, room, roomReservation
from reservation_api.serializers import reservationSerializer
from Image.models import picture


class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = picture
        fields = '__all__'


class roomTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = roomType
        fields = '__all__'


class roomSerializer(serializers.ModelSerializer):
    typeID = roomTypeSerializer(read_only=False)
    pictureID = imageSerializer()

    class Meta:
        model = room
        fields = '__all__'

    # def create(self, validate_data):
    #     rooms_data = validate_data.pop('typeID')
    #     pics =validate_data.pop('pictureID')
    #     Room= room.objects.create(**validate_data)
    #     # for room_data in rooms_data:
    #     #     roomType.objects.create(Room=Room,**room_data)

    #     for pic in pics:
    #         picture.objects.create(Room=Room,**pic)

    #     return Room


class roomReservationSerializer(serializers.ModelSerializer):
    roomID = roomSerializer()
    reservationID = reservationSerializer()

    class Meta:
        model = roomReservation
        fields = '__all__'
