"""aws_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

import web_app.views
import rest_app.views

router = routers.DefaultRouter()
router.register(r'poolstats', rest_app.views.PoolStatsViewSet)
router.register(r'latestpoolstats', rest_app.views.LatestPoolStatsViewSet)
router.register(r'officestats', rest_app.views.OfficeStatsViewSet)
router.register(r'latestofficestats', rest_app.views.LatestOfficeStatsViewSet)
router.register(r'latestpatiostats', rest_app.views.LatestOutsidePatioTempViewSet)
router.register(r'outsidepatiotemp', rest_app.views.OutsidePatioTempViewSet)
router.register(r'fronttemp', rest_app.views.FrontTempViewSet)
router.register(r'latestfronttemp', rest_app.views.LatestFrontTempViewSet)
router.register(r'pistats', rest_app.views.PiStatsViewSet)
router.register(r'humphreystats', rest_app.views.HumphreyStatsViewSet)
router.register(r'wundergroundweather', rest_app.views.WunderGroundWeatherViewSet)
router.register(r'fenixprices', rest_app.views.FenixPricesViewSet)
router.register(r'pollencount', rest_app.views.PollenCountViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^$', web_app.views.index, name='top'),
    url(r'^about/', web_app.views.about, name='about'),
    url(r'^fenix/', web_app.views.fenix, name='fenix'),
    url(r'^pistats/', web_app.views.pistats, name='pistats'),
    url(r'^tm/', web_app.views.tm, name='tm'),
    url(r'^humphrey/', web_app.views.humphrey, name='humphrey'),
    url(r'^temperature/', web_app.views.temperature, name='temperature'),
    url(r'^weather/', web_app.views.weather, name='weather'),
    url(r'^apidocs/', include_docs_urls(title='apidocs')),
    url(r'^pollencount/', web_app.views.pollen, name='pollen'),

]
