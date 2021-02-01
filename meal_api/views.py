from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from meal.models import mealType, meal
from django.shortcuts import get_object_or_404
from .serializers import mealTypeSerializer, mealSerializer


class mealTypeList(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = mealType.objects.all()
    serializer_class = mealTypeSerializer


class mealList(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = meal.objects.all()
    serializer_class = mealSerializer
