#!/usr/bin/env python
from panelbase import PanelBase
from rgbmatrix import graphics
from get_data import *
from config import *
from datetime import datetime, timedelta
import requests
import time
import json

fname = "5x7.bdf"
tnow = datetime.now()
timers = {
    "1min" : tnow.minute,
    "5min" : tnow.minute,
    "1hour": tnow.hour,
    "Pollen_time": [6, True],
    "Humphrey_time": [8, True],
    "Off_time": [20, 6],
    "On_time": [6, 20],
    "Dweet": "off",
}

getDweet = "https://dweet.io/get/latest/dweet/for/DWEET_IO_ENDPOINT"

class MatrixPanel(PanelBase):

    def __init__(self, *args, **kwargs):
        super(MatrixPanel, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/" + fname)
        kfont = graphics.Font()
        kfont.LoadFont("../../../fonts/kling.bdf")
        time_pos = canvas.width
        while True:

            tnow = datetime.now()

            if tnow.minute == timers["1min"]:
                print("running 1 minute timer {}".format(datetime.now().strftime('%H:%M:%S')))
                orb_color = get_orb()
                pi_hole_stats()
                try:
                    dweet_on = requests.get(getDweet).json()
                    if "off" in dweet_on["with"][0]["content"]["board"]:
                        timers["Dweet"] = "off"
                except:
                    pass
                timers["1min"] = (tnow + timedelta(minutes=1)).minute

            if tnow.minute == timers["5min"]:
                print("running 5 minute timer {}".format(datetime.now().strftime('%H:%M:%S')))
                office_color = get_office_temp()
                front_color = get_front_temp()
                patio_color = get_patio_temp()
                get_high_temp()
                timers["5min"] = (tnow + timedelta(minutes=5)).minute

            if tnow.hour == timers["1hour"]:
                print("running 1 hour timer {}".format(datetime.now().strftime('%H:%M:%S')))
                timers["1hour"] = (tnow + timedelta(hours=1)).hour

            if tnow.hour == timers["Pollen_time"][0] and timers["Pollen_time"][1] == True:
                get_pollen()
                print("running Pollen Timer {}".format(datetime.now().strftime('%H:%M:%S')))
                timers["Pollen_time"][1] = False

            if tnow.hour == timers["Humphrey_time"][0] and timers["Humphrey_time"][1] == True:
                humphrey_stats()
                print("running Humphrey Timer {}".format(datetime.now().strftime('%H:%M:%S')))
                timers["Humphrey_time"][1] = False

            if tnow.hour == 7 and timers["Humphrey_time"][1] == False:
                print("reseting Pollen and Humphrey Timer {}".format(datetime.now().strftime('%H:%M:%S')))
                timers["Humphrey_time"][1] = True
                timers["Pollen_time"][1] = True

            blue_2 = graphics.Color(42, 83, 52)
            blue3 = graphics.Color(0, 75, 33) 
            dark_green = graphics.Color(12, 27, 36)
            gold = graphics.Color(91, 43, 81)
            orange2 = graphics.Color(129, 1, 54)
            hot_pink = graphics.Color(101, 80, 1)
            grey = graphics.Color(27, 40, 34)
            blue3 = graphics.Color(0, 75, 33)

            orb_rbg_color = graphics.Color(data_dict['orb_color'][0], data_dict['orb_color'][1], data_dict['orb_color'][2])
            office_rbg_color = graphics.Color(data_dict['office_color'][0], data_dict['office_color'][1], data_dict['office_color'][2])
            front_rbg_color = graphics.Color(data_dict['front_color'][0], data_dict['front_color'][1], data_dict['front_color'][2])
            patio_rbg_color = graphics.Color(data_dict['patio_color'][0], data_dict['patio_color'][1], data_dict['patio_color'][2])
            uv_rbg_color =  graphics.Color(data_dict['uv_color'][0], data_dict['uv_color'][1], data_dict['uv_color'][2])

            if (tnow.hour >= timers["On_time"][0] and tnow.hour < timers["On_time"][1]) or timers["Dweet"] == "on":
                time_now = get_time()
                canvas.Clear()

                graphics.DrawText(canvas, font, 0, 6, blue_2, "Office")
                graphics.DrawText(canvas, font, 40, 6, office_rbg_color, "{:.4}".format(data_dict['office_lst'][-1]))

                graphics.DrawText(canvas, font, 0, 13, blue_2, "Front")
                graphics.DrawText(canvas, font, 40, 13, front_rbg_color, "{:.4}".format(data_dict['front_lst'][-1]))

                graphics.DrawText(canvas, font, 0, 20, blue_2, "Patio")
                graphics.DrawText(canvas, font, 40, 20, patio_rbg_color, "{:.4}".format(data_dict['patio_lst'][-1]))

                graphics.DrawText(canvas, font, 0, 29, dark_green, "UV")        
                graphics.DrawText(canvas, font, 40, 29, uv_rbg_color, "{}".format(data_dict['current_uv']))

                graphics.DrawText(canvas, font, 0, 38, dark_green, "Curr")                                  
                graphics.DrawText(canvas, font, 40, 38, orange2, "{:.4}".format(float(data_dict['current_location_temp']))) 

                graphics.DrawText(canvas, font, 0, 45, dark_green, "Feels")                
                graphics.DrawText(canvas, font, 40, 45, orange2, "{:.4}".format(float(data_dict['current_feels_like']))) 

                graphics.DrawText(canvas, font, 0, 52, dark_green, "RH")                
                graphics.DrawText(canvas, font, 40, 52, orange2, "{}".format(data_dict['current_humidity'])) 

                graphics.DrawText(canvas, font, 0, 63, dark_green, "High")                
                graphics.DrawText(canvas, font, 40, 63, blue3, "{:.4}".format(data_dict['todays_high'])) 

                graphics.DrawText(canvas, font, 64, 6, dark_green, "Pollen")
                graphics.DrawText(canvas, font, 104, 6, blue3, "{}".format(data_dict['pollen']))

                graphics.DrawText(canvas, font, 64, 17, dark_green, "Humphrey")
                graphics.DrawText(canvas, font, 109, 17, gold, "{}".format(int(data_dict['humphrey_laps'])))

                graphics.DrawText(canvas, font, 64, 28, dark_green, "DNS Q")
                graphics.DrawText(canvas, font, 104, 28, grey, "{}".format(int(data_dict['pi_hole_status_24hr_DNS_queries'])))      

                graphics.DrawText(canvas, font, 64, 35, dark_green, "Ads")
                graphics.DrawText(canvas, font, 109, 35, grey, "{}".format(int(data_dict['pi_hole_stats_24hr_block'])))    

                time_indent = 64 + ((64 - (len(time_now) * 5)) // 2)
                graphics.DrawText(canvas, kfont, time_indent, 62, orb_rbg_color, time_now)

                canvas = self.matrix.SwapOnVSync(canvas) #Testing
                time.sleep(.07)

            elif tnow.hour < timers["On_time"][0] or tnow.hour >= timers["Off_time"][1]:
                try:
                    dweet_on = requests.get(getDweet).json()
                    if "on" in dweet_on["with"][0]["content"]["board"]:
                        timers["Dweet"] = "on"
                    else:
                        canvas.Fill(0,0,0)
                        canvas = self.matrix.SwapOnVSync(canvas) 
                        timers["Dweet"] = "off"
                        time.sleep(60)
                except:
                    pass

def initial_list_seed():
    tnow = datetime.now()
    data_dict['office_lst'] = []
    data_dict['patio_lst'] = []
    data_dict['front_lst'] = []
    timers["1min"] = tnow.minute
    timers["5min"] = tnow.minute
    timers["1hour"] = tnow.hour

    r = requests.get(url + "officestats/1/", headers=head)
    results = r.json()
    data_dict['office_temperature'] = results['office_temperature']

    r = requests.get(url + "latestpatiostats/", headers=head)
    results = r.json()
    data_dict['outside_patio_temperature'] = results[0]['outside_patio_temperature']

    r = requests.get(url + "latestfronttemp/", headers=head)
    results = r.json()
    data_dict['front_temperature'] = results[0]['front_temperature']

    pi_hole_stats()
    get_high_temp()
    get_pollen() 
    humphrey_stats()

    for i in range (5):
        data_dict['office_lst'].append(data_dict['office_temperature'])
        data_dict['patio_lst'].append(data_dict['outside_patio_temperature'])
        data_dict['front_lst'].append(data_dict['front_temperature'])

if __name__ == "__main__":
    initial_list_seed()
    matrix_panel = MatrixPanel()
    if (not matrix_panel.process()):
        matrix_panel.print_help()