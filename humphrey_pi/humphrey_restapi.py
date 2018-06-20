import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
import urllib

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#  ThingSpeak Channel Settings
channelID = "XXXXX"  # Prod Channel
apiKey = "API_KEY_HERE"  # Prod Key


#io pin 17 for hall effect sensor
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Setup the display
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.rectangle((0,0,width,height), outline=0, fill=0)

resetKey = 0
resetTimeKey = 1
revLength = 63.5
rotationCount = 0
totalDist = 0.0
totalCM = 0
totalCM = 0
totalKM = 0
totalM = 0

while True:

    timestamp = time.strftime('%I:%M:%S:%p')
    time_string = timestamp.split(":")

    if (int(time_string[0]) == 7) and (int(time_string[1]) == 0) and (time_string[3] == "AM") and resetTimeKey == 1:
        print("Sending Data")
        totalCM = rotationCount * revLength
        totalCM = rotationCount * revLength
        totalKM = float("{0:.4f}".format(totalCM * 0.00001))
        totalM = float("{0:.4f}".format(totalCM * 0.000006213711922))
        params = urllib.urlencode({'key': apiKey, 'field1': rotationCount, 'field2': totalKM, 'field3': totalM})
        urllib.urlopen("https://api.thingspeak.com/update", data=params)
        rotationCount = 0
        resetTimeKey = 0

    if (int(time_string[1]) >= 1) and resetTimeKey == 0:
        print("Resetting Time Key")
        resetTimeKey = 1

    if (GPIO.input(buttonPin) == False) and (resetKey == 0):
        rotationCount += 1
        resetKey = 1
        print("@ {} - incrementing by 1 {}".format(time.asctime(), rotationCount))
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        disp.display()
        draw.text((0, 0), "- Humphrey Counter -", font=font, fill=255)
        draw.text((0, 22), "Lap: " + str(rotationCount), font=font, fill=255)
        draw.text((0, 14), "Last @ " + timestamp, font=font, fill=255)
        disp.image(image)
        disp.display()
        with open("humphrey.txt", 'w') as humphrey_result_file:
            humphrey_result_file.write("Rotation Count {}\n".format(rotationCount))

    elif (GPIO.input(buttonPin) == False) and (resetKey == 1):
        # do nothing
        time.sleep(.001)

    elif (GPIO.input(buttonPin) == True) and (resetKey == 1):
        resetKey = 0

    else:
        resetKey = 0

