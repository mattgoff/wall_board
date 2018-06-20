import time
import requests
import RPi.GPIO as GPIO

url= "https://dweet.io/dweet/for/MY_DWEET_POINT?board="
getDweet = "https://dweet.io/get/latest/dweet/for/MY_DWEET_POINT"

GPIO.setmode(GPIO.BCM)
capPin = 25
GPIO.setup(capPin, GPIO.IN)

print("Here we go! Press CTRL+C to exit")

while True:
    # dweetStatus = requests.get(getDweet).json()
    # dweetStatus["with"][0]["content"]["board"]
    # "on" in dweetStatus["with"][0]["content"]["board"]
    try:
        if GPIO.input(capPin) == 1:
            print("Turn on")
            try:
                requests.get(url + "on")
            except:
                pass
        else:
            print("Turn off")
            try:
                requests.get(url + "off")
            except:
                pass
        time.sleep(30)

    except KeyboardInterrupt:
        GPIO.cleanup()
        pass