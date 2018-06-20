from config import *
import requests
import time
import ast 
import datetime
import json

def get_office_temp():
    try:
        r = requests.get(url + "officestats/1/", headers=head)
        results = r.json()
        data_dict['office_lst'].append(results['office_temperature'])
        data_dict['office_lst'].pop(0)
        avg_office_temp = (sum(data_dict['office_lst'][:-1]) / (len(data_dict['office_lst']) - 1 ))
        print("Office - {} - avg {} last {}".format(data_dict['office_lst'][:-1], avg_office_temp, results['office_temperature']))
        if avg_office_temp < results['office_temperature']:
            data_dict['office_color'] = [81, 9, 10]
        elif avg_office_temp > results['office_temperature']:
            data_dict['office_color'] = [17, 0, 68]
        else:
            data_dict['office_color'] = [27, 148, 33]
    except:
        print("error getting office stats")
        data_dict['office_color'] = [178, 255, 0]        

def get_front_temp():
    try:
        r = requests.get(url + "latestfronttemp/", headers=head)
        results = r.json()  
        data_dict['front_lst'].append(results[0]['front_temperature']) 
        data_dict['front_lst'].pop(0)
        avg_front_temp = (sum(data_dict['front_lst'][:-1]) / (len(data_dict['front_lst']) -1 ))
        print("Front - {} - Avg {} last {}".format(data_dict['front_lst'][:-1], avg_front_temp, results[0]['front_temperature']))
        if avg_front_temp < results[0]['front_temperature']:
            data_dict['front_color'] = [81, 9, 10]
        elif avg_front_temp > results[0]['front_temperature']:
            data_dict['front_color'] =  [17, 0, 68]
        else:
            data_dict['front_color'] =  [27, 148, 33]
    except:
        print("error getting front stats")
        data_dict['front_color'] = [178, 255, 0]     

def get_patio_temp():
    try:
        r = requests.get(url + "latestpatiostats/", headers=head)
        results = r.json()
        data_dict['patio_lst'].append(results[0]['outside_patio_temperature']) 
        data_dict['patio_lst'].pop(0)
        avg_patio_temp = (sum(data_dict['patio_lst'][:-1]) / (len(data_dict['patio_lst']) -1 ))
        print("Patio - {} - Avg {} last {}".format(data_dict['patio_lst'][:-1], avg_patio_temp, results[0]['outside_patio_temperature']))
        if avg_patio_temp < results[0]['outside_patio_temperature']:
            data_dict['patio_color'] = [81, 9, 10]
        elif avg_patio_temp > results[0]['outside_patio_temperature']:
            data_dict['patio_color'] = [17, 0, 68]
        else:
            data_dict['patio_color'] = [27, 148, 33]
    except:
        print("error getting patio stats")
        data_dict['patio_color'] = [178, 255, 0]   

def get_pollen():
    try:
        r = requests.get(url + "pollencount/", headers=head)
        results = r.json()
        pc = str(results[0]['pollen_today'].split()[0])
        data_dict['pollen'] = pc
    except:
        print("error connecting to pollen.com")

def get_time():
    time_now = datetime.datetime.now().strftime('%-I:%M:%S %p')
    return time_now

def get_high_temp():
    try:
        r = requests.get(url + "wundergroundweather/", headers=head)
        results = r.json()
        data_dict['todays_high'] = ast.literal_eval(results[0]['wunderground_4day_0_day'])['high']
        data_dict['current_uv'] = ast.literal_eval(results[0]['wunderground_current'])['current_uv']

        data_dict['current_location_temp'] = ast.literal_eval(results[0]['wunderground_current'])['current_location_temp']
        data_dict['current_feels_like'] = ast.literal_eval(results[0]['wunderground_current'])['current_feels_like']
        data_dict['current_humidity'] = ast.literal_eval(results[0]['wunderground_current'])['current_humidity']

        uv = float(data_dict['current_uv'])
        if 0 <= uv and uv <= 2.9:
            data_dict['uv_color'] = [16,0,60] 
        elif 3 <= uv <= 5.9:
            data_dict['uv_color'] = [102,0,102]
        elif 6 <= uv <= 7.9:
            data_dict['uv_color'] = [101,0,51]  
        elif 8 <= uv <= 10.9:
            data_dict['uv_color'] = [102,0,0] 
        elif uv >= 11:
            data_dict['uv_color'] = [56,96, 6]   
        else:
            data_dict['uv_color'] = [10, 59, 13] 
    except:
        print("error connecting to wunderground")

def pi_hole_stats():
    try:
        r = requests.get("http://172.16.12.9/admin/api.php")
        results = ast.literal_eval(r.content)
        data_dict['pi_hole_status_24hr_DNS_queries'] = results['dns_queries_today']
        data_dict['pi_hole_stats_24hr_block'] = results['ads_blocked_today']
    except:
        print("error connecting to pi-stats")

def humphrey_stats():
    try:
        r = requests.get("https://api.thingspeak.com/channels/284894/feeds.json?results=1")
        results = r.json()
        data_dict['humphrey_laps'] = str(results['feeds'][0]['field1'])
    except:
        print("error connecting to humphrey stats")

def get_orb():
    try:
        r = requests.get("https://dweet.io:443/get/latest/dweet/for/WORK_MONITOR_DWEET_ENDPOINT")
        data = r.text
        dweet = json.loads(r.text)
        status = dweet['with'][0]['content']['cmd']
        # print(status)
        if 'Normal' in status:
             data_dict['orb_color'] = [17, 0, 68]
        elif 'Major' in status:
            data_dict['orb_color'] = [204, 0, 51]
        elif 'Warning' in status:
            data_dict['orb_color'] = [255, 0, 204]
        elif 'Critical' in status:
            data_dict['orb_color'] = [255, 0, 204]
    except:
        print("error connecting to orb")
        data_dict['orb_color'] = [107, 35, 142] 