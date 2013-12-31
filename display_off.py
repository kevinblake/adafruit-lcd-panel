#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from Adafruit_I2C import Adafruit_I2C
from time import sleep

if __name__ == '__main__':
    lcd = Adafruit_CharLCDPlate(busnum = 1)
    lcd.begin(16, 2)
    lcd.noDisplay()
    lcd.stop()