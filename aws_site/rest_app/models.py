from django.db import models

# Create your models here.
class PoolStats(models.Model):
    pool_temperature = models.FloatField()
    pool_ph = models.FloatField()
    pool_recorded_at = models.DateTimeField(auto_now=True)

class OfficeStats(models.Model):
    office_temperature = models.FloatField()
    office_humidity = models.FloatField()
    office_recorded_at = models.DateTimeField(auto_now=True)

class OutsidePatioTemp(models.Model):
    outside_patio_temperature = models.FloatField()
    outside_patio_recorded_at = models.DateTimeField(auto_now=True)

class FrontTemp(models.Model):
    front_temperature = models.FloatField()
    front_recorded_at = models.DateTimeField(auto_now=True)

class PiStats(models.Model):
    pi_hole_stats_24hr_block = models.FloatField()
    pi_hole_status_24hr_DNS_queries = models.FloatField()
    pi_hole_cpu_temperature = models.FloatField()
    pi_hole_stats_recorded_at = models.DateTimeField(auto_now=True)

class HumphreyStats(models.Model):
    humphrey_laps = models.IntegerField()
    humphrey_miles = models.FloatField()
    humphrey_kilometers = models.FloatField()
    humphrey_recorded_at = models.DateTimeField(auto_now=True)

class WunderGroundWeather(models.Model):
    wunderground_current = models.TextField()
    wunderground_4day_0_day = models.TextField()
    wunderground_4day_1_day = models.TextField()
    wunderground_4day_2_day = models.TextField()
    wunderground_4day_3_day = models.TextField()
    wunderground_current_time = models.DateTimeField(auto_now=True)

class FenixPrices(models.Model):
    fenix_store_name = models.TextField()
    fenix_store_price = models.TextField()
    fenix_store_url = models.TextField()
    fenix_recorded_at = models.DateTimeField(auto_now=True)

class PollenCount(models.Model):
    pollen_yesterday = models.TextField()
    pollen_today = models.TextField()
    pollen_tomorrow = models.TextField()
    
