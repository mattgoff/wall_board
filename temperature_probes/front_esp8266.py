import machine
import urequests
import network
import ntptime
import time
import ds18x20
import onewire

verString = "1.7"

ow = onewire.OneWire(machine.Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

reset_time_check = 1
ntp_reset = 1
reset_time = 0

send_url = "http://www.goff.us/api/fronttemp/"
auth_token = "its_a_secret"
head = {'Authorization': 'token {}'.format(auth_token), 'Content-Type': 'application/json'}

body_data = {}

def do_connect():
    WIFISSID = '4ghome'
    WIFIPASS = 'welcome22'
    # from network import WLAN
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFISSID, WIFIPASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def upload(tempin):
    try:
        body_data = {'front_temperature': tempin}
        print(body_data)
        response = urequests.post(send_url, json=body_data, headers=head)
    except:
        pass

def ntpupdate():
    try:
        ntptime.host = "172.16.12.9"
        ntptime.settime()
    except:
        pass

def getcurrenttime():
    time_tuple = time.localtime()
    tuple_hour = time_tuple[3]
    tuple_minute = time_tuple[4]
    hour_12 = ((tuple_hour + 11) % 12 + 1)
    hour_list = [0, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5]
    hour_local = hour_list[hour_12]
    if tuple_minute < 10:
        minute_local = "0{}".format(tuple_minute)
    else:
        minute_local = tuple_minute
    return hour_local, minute_local

def gettemp():
    try:
        ds.convert_temp()
        time.sleep(1)
        tempc = ds.read_temp(roms[0])
        tempin = (tempc * (9 / 5)) + 32
        return tempin
    except:
        pass

do_connect()
ntpupdate()

time.sleep(15)

while True:

    if (int(getcurrenttime()[1]) % 5) == 0 and reset_time_check == 1:
        get_current_front_temp = gettemp()
        upload(get_current_front_temp)
        print("Sending Data")
        reset_time_check = 0
        reset_time = int(getcurrenttime()[1]) + 1

    if int(getcurrenttime()[1]) == reset_time and reset_time_check == 0:
        print("Resetting time_check")
        reset_time_check = 1

    if int(getcurrenttime()[0] == 12) and reset_time_check == 1 and ntp_reset == 1:
        print("updating NTP")
        ntpupdate()
        ntp_reset = 0

    if ntp_reset == 0 and int(getcurrenttime()[0]) == 1:
        print("Resetting ntp_reset key")
        ntp_reset = 1
