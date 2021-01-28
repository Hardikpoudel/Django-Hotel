from rest_framework import serializers
from guest.models import guest


class guestSerializer(serializers.ModelSerializer):
    class Meta:
        model = guest
        fields = '__all__'
