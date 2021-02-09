from rest_framework import serializers
from room.models import roomType, room, roomReservation
from reservation_api.serializers import reservationSerializer
from Image.models import picture
import os
from pathlib import Path


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
    # typeID = roomTypeSerializer(read_only=False)
    # pictureID = imageSerializer()

    class Meta:
        model = room
        fields = '__all__'

    # representation of the dropdown listview of items
    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['typeID'] = roomTypeSerializer(instance.typeID).data
        picture = imageSerializer(instance.pictureID).data
        picture_path = "http://192.168.0.103:8888"+str(picture["photo"])
        picture["photo"] = picture_path
        response['imageID'] = picture
        return response

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['pictureID'] = imageSerializer(instance.pictureID).data
    #     return response

# class ProductVariationsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = product_variations
#         fields = "__all__"
#     def to_representation(self,instance):
#         response = super().to_representation(instance)
#         response['product_id'] = ProductsSerializer(instance.product_id).data
#         return response
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
