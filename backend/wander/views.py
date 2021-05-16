from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from rest_framework import viewsets

from .models import Attraction, Place, PosterEvent, Restaurant, City
from .serializers import AttractionSerializer, RestaurantSerializer, \
    PosterEventSerializer, CitySerializer, PlaceSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all().order_by('place__name')
    serializer_class = AttractionSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer


class PosterEventViewSet(viewsets.ModelViewSet):
    queryset = PosterEvent.objects.all()
    serializer_class = PosterEventSerializer
