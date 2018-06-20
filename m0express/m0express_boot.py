import board
import neopixel
import time
from digitalio import DigitalInOut
 
pixpin = board.D1
numpix = 5
bright = 3

ledrun = DigitalInOut(board.D5)
ledrun.Pull.DOWN
ledrun.Direction.IN

strip = neopixel.NeoPixel(pixpin, numpix)

onboard = pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
onboard.fill((0,0,0))
onboard.write()
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3) // bright, int(255 - (pos*3)) // bright, 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3) // bright, 0, int(pos*3) // bright)
    else:
        pos -= 170
        return (0, int(pos*3) // bright, int(255 - pos*3) // bright)
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(5):
            idx = int ((i * 256 / 5) + j)
            strip[i] = wheel(idx & 255)
        strip.write()
        time.sleep(wait)

def turn_off():
    strip.fill((0,0,0))
    strip.write()

while True:
    if ledrun.value == True:
        rainbow_cycle(0.3)    # rainbowcycle with 1ms delay per step
    else:
        turn_off()
        time.sleep(60)





