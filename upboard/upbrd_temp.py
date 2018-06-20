from Adafruit_BME280 import *
import requests

url = "http://www.goff.us/api/officestats/1/"
auth_token = "its_a_secret"
head = {'Authorization': 'token {}'.format(auth_token)}

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

body_data = {}

humidity = None
temperature = None

def send_info(humidity, temperature):
    body_data.update({'office_temperature': temperature})
    body_data.update({'office_humidity': humidity})
    try:
        response = requests.put(url, headers=head, data=body_data)
        data = response.json()
        print(data)
    except:
        pass

def get_temp():
    degrees = sensor.read_temperature()
    degreesF = (degrees * (9.0 / 5.0))+ 32
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()
    # print 'Temp      = {0:0.3f} deg F'.format(degreesF)
    # print 'Humidity  = {0:0.2f} %'.format(humidity)
    return humidity, degreesF

humidity, temp_f = get_temp()
send_info(humidity, temp_f)
