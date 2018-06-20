import requests
import json 

forecast_4day = "" 
forecast_4day_text = ""
weather_dict = {'wunderground_current':{}}

def do_weather():
    print("Updating Weather")
    global forecast_4day
    global forecast_4day_text

    try:
        current_conditions = requests.get(
            'http://api.wunderground.com/api/WUNDERGROUND_API_HERE/conditions/forecast/q/pws:KAZPEORI95.json')
        current_cond_parsed_json = current_conditions.json()

        weather_dict['wunderground_current']['location_city'] = current_cond_parsed_json['current_observation']['display_location']['city']
        weather_dict['wunderground_current']['location_state'] = current_cond_parsed_json['current_observation']['display_location']['state']
        weather_dict['wunderground_current']['current_location_temp'] = current_cond_parsed_json['current_observation']['temp_f']
        weather_dict['wunderground_current']['current_humidity'] = current_cond_parsed_json['current_observation']['relative_humidity']
        wind_speed = current_cond_parsed_json['current_observation']['wind_mph']
        wind_dir = current_cond_parsed_json['current_observation']['wind_dir']
        gust_speed = current_cond_parsed_json['current_observation']['wind_gust_mph']
        weather_dict['wunderground_current']['current_wind'] =  "{} {}".format(wind_speed, wind_dir)
        weather_dict['wunderground_current']['current_gust'] =  "{} {}".format(gust_speed, wind_dir)
        weather_dict['wunderground_current']['current_feels_like'] = current_cond_parsed_json['current_observation']['feelslike_f']
        weather_dict['wunderground_current']['current_solarradiation'] = current_cond_parsed_json['current_observation']['solarradiation']
        weather_dict['wunderground_current']['current_uv'] = current_cond_parsed_json['current_observation']['UV']
        weather_dict['wunderground_current']['current_icon'] = current_cond_parsed_json['current_observation']['icon_url']
        forecast_4day = current_cond_parsed_json['forecast']['simpleforecast']['forecastday']
        forecast_4day_text = current_cond_parsed_json['forecast']['txt_forecast']['forecastday']
        current_conditions.close()
    except IOError:
        print("Connection Error")
        pass

def create_dict(dict_index, x):
    weather_dict[dict_index] = {
        'day': forecast_4day[x]['date']['weekday_short'],
        'high': forecast_4day[x]['high']['fahrenheit'],
        'low': forecast_4day[x]['low']['fahrenheit'],
        'humidity': forecast_4day[x]['avehumidity'],
        'maxwind': str(forecast_4day[x]['maxwind']['mph']) + " " + forecast_4day[x]['maxwind']['dir'],
        'avewind': str(forecast_4day[x]['avewind']['mph']) + " " + forecast_4day[x]['avewind']['dir'],
        'day_text': forecast_4day_text[x*2]['fcttext'],
        'day_icon': forecast_4day_text[x*2]['icon_url'],
        'title_day': forecast_4day_text[x*2]['title'],
        'night_text': forecast_4day_text[(x*2)+1]['fcttext'],
        'night_icon': forecast_4day_text[(x*2)+1]['icon_url'],
        'title_night': forecast_4day_text[(x*2)+1]['title'],
    }


def get_weather_forecast():
    do_weather()

    for x in range(4):
        dict_key = "wunderground_4day_{}_day".format(x)
        create_dict(dict_key, x)


url = "http://www.goff.us/api/wundergroundweather/1/"
auth_token = "its_a_secret"

header_data = {
    "Content-Type":"application/json",
    'Authorization': 'token {}'.format(auth_token)
}

def send_info():
    if "74" not in weather_dict['wunderground_4day_0_day']['high']:
        weather_json = json.dumps(weather_dict)
        response = requests.put(url, headers=header_data, data=weather_json)
        data = response.json()
    else:
        print("Found 74 as high, skipping")
        pass

get_weather_forecast()
send_info()

