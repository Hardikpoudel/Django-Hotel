from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from reservation.models import reservation
from django.shortcuts import get_object_or_404
from .serializers import reservationSerializer


class reservationList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = reservation.objects.all()
    serializer_class = reservationSerializer
