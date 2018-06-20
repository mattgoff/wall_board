from rest_framework import serializers
from .models import PoolStats, OfficeStats, OutsidePatioTemp, PiStats
from .models import HumphreyStats, WunderGroundWeather, FenixPrices, PollenCount, FrontTemp

class PoolStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PoolStats
        fields = ('pool_temperature', 'pool_ph', 'pool_recorded_at')


class OfficeStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeStats
        fields = ('office_temperature', 'office_humidity', 'office_recorded_at')


class OutsidePatioTempSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutsidePatioTemp
        fields = ('outside_patio_temperature', 'outside_patio_recorded_at')

class FrontTempSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrontTemp
        fields = ('front_temperature', 'front_recorded_at')

class PiStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PiStats
        fields = ('pi_hole_stats_24hr_block', 'pi_hole_status_24hr_DNS_queries',
                    'pi_hole_cpu_temperature', 'pi_hole_stats_recorded_at')


class HumphreyStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HumphreyStats
        fields = ('humphrey_laps', 'humphrey_miles', 'humphrey_kilometers', 'humphrey_recorded_at')


class WunderGroundWeatherSerializer(serializers.ModelSerializer):
    wunderground_current = serializers.JSONField()
    wunderground_4day_0_day = serializers.JSONField()
    wunderground_4day_1_day = serializers.JSONField()
    wunderground_4day_2_day = serializers.JSONField()
    wunderground_4day_3_day = serializers.JSONField()
    class Meta:
        model = WunderGroundWeather
        fields = ('wunderground_current', 'wunderground_4day_0_day', 'wunderground_4day_1_day',
                 'wunderground_4day_2_day', 'wunderground_4day_3_day', 'wunderground_current_time') 

class FenixPricesSerialzer(serializers.ModelSerializer):

    class Meta:
        model = FenixPrices
        fields = ('fenix_store_name', 'fenix_store_price', 'fenix_store_url', 'fenix_recorded_at')


class PollenCountSerializer(serializers.ModelSerializer):

    # pollen_tomorrow = serializers.StringRelatedField(many=True)
    # pollen_today = serializers.StringRelatedField(many=True)
    # pollen_yesterday = serializers.StringRelatedField(many=True)

    class Meta:
        model = PollenCount
        fields = ('pollen_yesterday', 'pollen_today', 'pollen_tomorrow')