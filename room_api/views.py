from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from Image.models import picture
from room.models import roomType, room, roomReservation
from .serializers import roomTypeSerializer, roomSerializer, roomReservationSerializer, imageSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class imageList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = picture.objects.all()
    serializer_class = imageSerializer


class roomTypeList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = roomType.objects.all()
    serializer_class = roomTypeSerializer


# class roomList(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = room.objects.all()
#     serializer_class = roomSerializer


class roomList(viewsets.ModelViewSet):
    # if filter_backends:

    serializer_class = roomSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['roomName', 'price']
    permission_classes = [AllowAny]
    # permission_classes = [(ActionBasedPermission,)]
    # action_permissions = {
    #     IsAdminUser: ['update', 'partial_update', 'destroy', 'create'],
    #     AllowAny: ['retrieve', 'list']
    # }
    queryset = room.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['roomName', 'typeID']

    def get_object(self, **kwargs):
        item = self.kwargs.get('pk')
        print(item)
        return get_object_or_404(room, roomSlug=item)

    # def get_queryset(self):
    #     return room.objects.all()


class roomReservationList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = roomReservation.objects.all()
    serializer_class = roomReservationSerializer
