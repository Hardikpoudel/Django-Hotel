from rest_framework import serializers
from meal.models import mealType, meal


class mealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = mealType
        fields = '__all__'


class mealSerializer(serializers.ModelSerializer):
    class Meta:
        model = meal
        fields = '__all__'
