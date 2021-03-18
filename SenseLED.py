#!/usr/bin/env python3
########################################################################
# Filename    : SenseLED.py
# Description : Control led with infrared Motion sensor.
# auther      : www.freenove.com
# modification: 2019/12/28hgh
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 12       # define ledPin
sensorPin = 11    # define sensorPin

GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode
GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            GPIO.output(ledPin,GPIO.HIGH) # turn on led
            print ('led turned on >>>')
        else :
            GPIO.output(ledPin,GPIO.LOW) # turn off led
            print ('led turned off <<<')
        time.sleep(1)



loop()

