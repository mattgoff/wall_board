from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .models import PoolStats, OfficeStats, OutsidePatioTemp, PiStats
from .models import HumphreyStats, WunderGroundWeather, FenixPrices, PollenCount, FrontTemp

from .serializers import PoolStatsSerializer, OfficeStatsSerializer, OutsidePatioTempSerializer
from .serializers import PiStatsSerializer, HumphreyStatsSerializer, WunderGroundWeatherSerializer
from .serializers import FenixPricesSerialzer, PollenCountSerializer, FrontTempSerializer

# Create your views here.

class PoolStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PoolStats.objects.all()
    serializer_class = PoolStatsSerializer

class LatestPoolStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PoolStats.objects.all().order_by('-pool_recorded_at')[:1]
    serializer_class = PoolStatsSerializer

class OfficeStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OfficeStats.objects.all()
    serializer_class = OfficeStatsSerializer

class LatestOfficeStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OfficeStats.objects.all().order_by('-office_recorded_at')[:1]
    serializer_class = OfficeStatsSerializer

class OutsidePatioTempViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OutsidePatioTemp.objects.all()
    serializer_class = OutsidePatioTempSerializer

class LatestOutsidePatioTempViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = OutsidePatioTemp.objects.all().order_by('-outside_patio_recorded_at')[:1]
    serializer_class = OutsidePatioTempSerializer

class FrontTempViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FrontTemp.objects.all()
    serializer_class = FrontTempSerializer

class LatestFrontTempViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FrontTemp.objects.all().order_by('-front_recorded_at')[:1]
    serializer_class = FrontTempSerializer


class PiStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PiStats.objects.all()
    serializer_class = PiStatsSerializer

class HumphreyStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = HumphreyStats.objects.all()
    serializer_class = HumphreyStatsSerializer

class WunderGroundWeatherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = WunderGroundWeather.objects.all()
    serializer_class = WunderGroundWeatherSerializer

class FenixPricesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = FenixPrices.objects.all()
    serializer_class = FenixPricesSerialzer

class PollenCountViewSet(viewsets.ModelViewSet):
    queryset = PollenCount.objects.all()
    serializer_class = PollenCountSerializer