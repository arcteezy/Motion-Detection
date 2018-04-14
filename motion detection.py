# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import os
import picamera
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
camera = picamera.PiCamera()
while True:
        GPIO.wait_for_edge(17, GPIO.RISING)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22,False)
        print("Taking Pic")
        camera.capture('image1.jpg')
        sleep(5)
        camera.capture('image2.jpg')
GPIO.output(22,True) ## Turn on GPIO pin 7
GPIO.cleanup()
