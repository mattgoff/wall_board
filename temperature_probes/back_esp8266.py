import ssd1306
import machine
import urequests
import network
import ntptime
import time
import ds18x20
import onewire

verString = "1.6"
# this is a copy of out_esp8266.py


ow = onewire.OneWire(machine.Pin(12))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

reset_time_check = 1
ntp_reset = 1
reset_time = 0

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3d)

url = "http://www.goff.us/api/outsidepatiotemp/"
auth_token = "its_a_secret"
head = {'Authorization': 'token {}'.format(auth_token), 'Content-Type': 'application/json'}

body_data = {}

def do_connect():
    WIFISSID = 'SSID_HERE'
    WIFIPASS = 'PSK_HERE'
    # from network import WLAN
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFISSID, WIFIPASS)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def upload(tempin, currenttime):
    try:
        body_data = {'outside_patio_temperature': tempin}
        response = urequests.post(url, json=body_data, headers=head)
    except:
        pass

    write_display(["Last Upld @ {}".format(currenttime), "Temp: {:0.2f} F".format(tempin)])


def ntpupdate():
    ntptime.host = "172.16.12.9"
    ntptime.settime()


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
    ds.convert_temp()
    time.sleep(1)
    tempc = ds.read_temp(roms[0])
    tempin = (tempc * (9 / 5)) + 32
    return tempin


def write_display(datatowrite):
    oled.fill(0)
    oled.show()
    oled.text(datatowrite[0], 0, 0)
    oled.text(datatowrite[1], 0, 10)
    oled.show()

do_connect()
ntpupdate()

write_display(["Booting", "Version {}".format(verString)])
time.sleep(15)

timestring = "{}:{}".format(getcurrenttime()[0], getcurrenttime()[1])
write_display(["Start @ {}".format(timestring), "Temp: {:0.2f} F".format(gettemp())])

while True:

    if (int(getcurrenttime()[1]) % 10) == 0 and reset_time_check == 1:
        timestring = "{}:{}".format(getcurrenttime()[0], getcurrenttime()[1])
        upload(gettemp(), timestring)
        write_display(["Last Upld @ {}".format(timestring), "Temp: {:0.2f} F".format(gettemp())])
        reset_time_check = 0
        reset_time = int(getcurrenttime()[1]) + 1

    if int(getcurrenttime()[1]) == reset_time and reset_time_check == 0:
        timestring = "{}:{}".format(getcurrenttime()[0], getcurrenttime()[1])
        print("Resetting time_check @ {}".format(timestring))
        reset_time_check = 1

    if int(getcurrenttime()[0] == 12) and reset_time_check == 1 and ntp_reset == 1:
        timestring = "{}:{}".format(getcurrenttime()[0], getcurrenttime()[1])
        print("updating NTP @ {}".format(timestring))
        ntpupdate()
        ntp_reset = 0

    if ntp_reset == 0 and int(getcurrenttime()[0]) == 1:
        timestring = "{}:{}".format(getcurrenttime()[0], getcurrenttime()[1])
        print("Resetting ntp_reset key @ {}".format(timestring))
        ntp_reset = 1



