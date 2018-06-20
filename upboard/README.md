# Up Board

The Up Board is the main data collector / aggregator.

Setup as crontab jobs:
* every 5 minutes - upbrd_temp.py
  * Pulls Office temp from I2C connected Temperature sensor (Panel D)
* every 5 minutes - update_upbrd_stats.py
  * Pulls CPU Temp and sends to Rest Endpoint
  * Pulls Pi-Hole stats and send to Rest Endpoint
* every 10 minutes - update_weather.py
  * Connected to Wunderground and pulls local weather, sends to Rest Endpoint
* every 6 hours - scrape_poll_com.py
  * Using Selenium connects to pollen.com and grabs local pollen data
 </br>
 
 On boot / reload the UpBoard runs the following scripts:
 
 * kickoff.py
    * Displays current time on 7 Segment display (Panel C)
    * Based on time will send hi / low to M0 Express which will enable / disable NeoPixel backlights
*  upbrd_cap.py
    * Monitors Capacitive touch sensor
    * On high sends out dweet to turn on/off 64 x 64 panel (after hours)
  
 
