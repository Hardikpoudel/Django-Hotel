from rest_framework import serializers
from reservation.models import reservation


class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = '__all__'
