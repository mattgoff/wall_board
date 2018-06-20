import ast 

from django.shortcuts import render
from web_app import humphreycount
from rest_app.models import PiStats
from rest_app.models import FenixPrices
from rest_app.models import OfficeStats
from rest_app.models import OutsidePatioTemp
from rest_app.models import PollenCount
from rest_app.models import WunderGroundWeather
from rest_app.models import FrontTemp

# Create your views here.
def index(request):
    return render(request, 'web_app/index.html')

def about(request):
    return render(request, 'web_app/about.html')

def fenix(request):
    queryset = {}
    for x in range(0,6):
        t_data = FenixPrices.objects.all().values()[x]
        name = t_data['fenix_store_name']
        queryset[name] = [t_data['fenix_store_name'], t_data['fenix_store_price'], t_data['fenix_recorded_at'], t_data['fenix_store_url']]
    return render(request, 'web_app/fenix.html', context=queryset)

def tm(request):
    return render(request, 'web_app/tm.html')

def humphrey(request):
    humphrey_dict = humphreycount.humphrey_stats()
    return render(request, 'web_app/humphrey.html', context=humphrey_dict)

def temperature(request):
    the_dict = {}
    front_data = FrontTemp.objects.order_by('-front_recorded_at')[:5]
    front_dict = {'front_data': front_data.values()}
    patio_data = OutsidePatioTemp.objects.order_by('-outside_patio_recorded_at')[:5]
    patio_dict = {'patio_data': patio_data.values()}
    office_dict = OfficeStats.objects.all().values()[0]
    the_dict.update(patio_dict)
    the_dict.update(front_dict)
    the_dict.update(office_dict)
    return render(request, 'web_app/temperature.html', context=the_dict)

def weather(request):
    queryset = {}
    queryset = WunderGroundWeather.objects.all().values()[0]
    for obj in queryset:
        if obj == "wunderground_current" or "4day" in obj:
            queryset[obj] = ast.literal_eval(queryset[obj])
    
    return render(request, 'web_app/weather.html', context=queryset)

def pistats(request):
    queryset = {}
    queryset = PiStats.objects.all().values()[0]
    return render(request, 'web_app/pistats.html', context=queryset)

def pollen(request):
    queryset = {}
    queryset = PollenCount.objects.all().values()[0]
    for obj in queryset:
        if "pollen" in obj:
            queryset[obj] = queryset[obj].split()
    print(queryset)
    return render(request, 'web_app/pollen.html', context=queryset)
