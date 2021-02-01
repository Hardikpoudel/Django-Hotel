from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from diningHall.models import diningHall, diningHallReservation
from django.shortcuts import get_object_or_404
from .serializers import hallSerializer, hallReservationSerializer


class hallList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = diningHall.objects.all()
    serializer_class = hallSerializer


class hallReservationList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = diningHallReservation.objects.all()
    serializer_class = hallReservationSerializer
