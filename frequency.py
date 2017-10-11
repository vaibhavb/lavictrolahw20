import RPi.GPIO as GPIO
import time
import os

ReedPin = 11
TiltPin = 16
ReedCount = 0
TiltValue = 0
ReadTilt = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ReedPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(TiltPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def destroy():
    GPIO.cleanup()

def handle(pin):
    global ReedCount, TiltChange, ReadTilt
    if (pin == ReedPin):
        ReedCount = ReedCount + 1
    if (pin == TiltPin):
        ReadTilt = not(ReadTilt)

if __name__ == '__main__':
    setup()
    try:
        print "Frequency counter"
        GPIO.add_event_detect(ReedPin, GPIO.RISING, handle)
        GPIO.add_event_detect(TiltPin, GPIO.FALLING, handle, bouncetime=2000)
        while True:
            time.sleep(0.3)
            print "Frequency: ", ReedCount
            TiltValue = GPIO.input(TiltPin)
            print "Tilt: ", TiltValue
            ReedCount = 0
    except KeyboardInterrupt:
        destroy()
