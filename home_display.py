#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import argparse, urllib2, time, json
import xml.dom.minidom as xDom
from Adafruit_I2C import Adafruit_I2C
from time import sleep
import datetime

# Python library for Adafruit RGB-backlit LCD plate for Raspberry Pi.
# Written by Adafruit Industries.  MIT license.

# This is essentially a complete rewrite, but the calling syntax
# and constants are based on code from lrvick and LiquidCrystal.
# lrvic - https://github.com/lrvick/raspi-hd44780/blob/master/hd44780.py
# LiquidCrystal - https://github.com/arduino/Arduino/blob/master/libraries/LiquidCrystal/LiquidCrystal.cpp

if __name__ == '__main__':

    lcd = Adafruit_CharLCDPlate(busnum = 1)
    lcd.begin(16, 2)
    lcd.clear()

    btn = ((lcd.SELECT, 'Select', lcd.ON),
           (lcd.LEFT  , 'Left'  , lcd.RED),
           (lcd.UP    , 'Up'    , lcd.BLUE),
           (lcd.DOWN  , 'Down'  , lcd.GREEN),
           (lcd.RIGHT , 'Right' , lcd.VIOLET))

    prev=1
#    for i in range(16, len(msg)):
#        sleep(0.25)
#        lcd.scrollDisplayLeft()
    while True:
        try:

            for b in btn:
                if lcd.buttonPressed(b[0]):
                    if b is not prev:
                        print b[1]
                        lcd.clear()
                        lcd.message(b[1])
                        lcd.backlight(b[2])
                        prev = b
                    break


            startTime = datetime.time(7,30,0,0)
            currentTime = datetime.datetime.now().time()
            endTime = datetime.time(9,15,0,0)

            if currentTime > startTime and currentTime < endTime:
                api = urllib2.urlopen("http://mybus.kb.tl/BusTimes/Json")

                data = json.load(api)

                arr1 = data['Locations'][0]['Arrivals'][0]
                arr2 = data['Locations'][0]['Arrivals'][1]

                message = arr1["RouteName"] + " " + arr1["WaitTime"] + ": " + arr1["ScheduledTime"] +  "\n" + arr2["RouteName"] + " " + arr2["WaitTime"] + ": " + arr2["ScheduledTime"]
                lcd.clear()
                lcd.message(message)
                sleep(30)
            else:
                lcd.clear()
                lcd.message(currentTime.strftime('%H:%M'))
                sleep(30)
        except Exception as inst:
            print "broken:"
            print inst
#    col = (('Red' , lcd.RED) , ('Yellow', lcd.YELLOW), ('Green' , lcd.GREEN),
#           ('Teal', lcd.TEAL), ('Blue'  , lcd.BLUE)  , ('Violet', lcd.VIOLET),
#           ('Off' , lcd.OFF) , ('On'    , lcd.ON))

#    print "Cycle thru backlight colors"
#    for c in col:
#       print c[0]
#       lcd.clear()
#       lcd.message(c[0])
#       lcd.backlight(c[1])
#       sleep(0.5)

    btn = ((lcd.SELECT, 'Select', lcd.ON),
           (lcd.LEFT  , 'Left'  , lcd.RED),
           (lcd.UP    , 'Up'    , lcd.BLUE),
           (lcd.DOWN  , 'Down'  , lcd.GREEN),
           (lcd.RIGHT , 'Right' , lcd.VIOLET))
    
 #   print "Try buttons on plate"
 #   lcd.clear()
 #   lcd.message("Try buttons")
    prev = -1
    while True:
        for b in btn:
            if lcd.buttonPressed(b[0]):
                if b is not prev:
                    print b[1]
                    lcd.clear()
                    lcd.message(b[1])
                    lcd.backlight(b[2])
                    prev = b
                break
