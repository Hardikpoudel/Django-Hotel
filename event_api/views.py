from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from event.models import event, eventReservation
from django.shortcuts import get_object_or_404
from .serializers import eventSerializer, eventReservationSerializer


class eventList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = event.objects.all()
    serializer_class = eventSerializer


class eventReservationList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = eventReservation.objects.all()
    serializer_class = eventReservationSerializer
