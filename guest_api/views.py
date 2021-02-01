from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, AllowAny
from guest.models import guest
from django.shortcuts import get_object_or_404
from .serializers import guestSerializer


class guestList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = guest.objects.all()
    serializer_class = guestSerializer
