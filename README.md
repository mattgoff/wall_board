# Slightly over engineered clock

What started out as a a simple 7 segment led clock driven by a Raspberry Pi, over time has turned into:


<img src="images/wall_board_labeled.jpg" width="400">

* A.  2x 64x64 led matrix panel
    * The first three lines are temperatures from different areas around the house.
    * Text color defined by last 20 minutes of temperature changes:
        *  Red - warming up
        *  Blue - unchanged
        *  Green - cooling down
    * Current UV rating outside
    * Current Temperature
    * Currently Feels like
    * RH - Relative Hummidity
    * High for the day
    * Pollen Count
    * Number of lap Humphrey (son's hamster) ran last night
    * DNS Queries over the last 24 hours as recorded by Pi-Hole
    * Number of Ads blocked over the 24 hours as recorded by Pi-Hole
    * Current time in my best attempt at a Klingon font
* B.  Raspberry pi with Adafruit 64x64 maxitrix bonnet
* C.  7 Segment LED with i2c backpack
* D.  I2C Temperautre sensor (left) / M0 Express running circuit python (right)
* E.  I2C bus and proto board
* F.  Upboard
* G.  Capacitive touch sensor
 
