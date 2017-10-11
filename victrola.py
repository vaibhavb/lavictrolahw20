import RPi.GPIO as GPIO
import time
import os
import signal
import subprocess
import random

ReedPin = 11 #pin11
TiltPin = 16 #pin16
ReedCount = 0
TiltValue = 0
Dirs = "/home/pi/Documents/my_projects/lavictrola/music/"
Files = []

def setup():
        global Files
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ReedPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(TiltPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        Files = os.listdir(Dirs)

def destroy():
        GPIO.cleanup()

def count_reed():
        global Count

def handle(pin):
    global ReedCount
    if (pin == ReedPin):
        ReedCount = ReedCount + 1


if __name__ == '__main__':
        setup()
        print "Starting the La Victrola program"
        try:
                proc_music_on = False
                GPIO.add_event_detect(ReedPin, GPIO.RISING, handle)
                while True:
                        time.sleep(0.3)
                        TiltValue = GPIO.input(TiltPin)                        
                        print "Reed: ", ReedCount
                        print "Tilt: ", TiltValue
                        if ((ReedCount >= 1) and (TiltValue == 1)) :
                                if (proc_music_on == False) :
                                        print("Starting music .. !")
                                        music = random.choice(Files)
                                        music_file = Dirs + music
                                        proc_music = subprocess.Popen(['omxplayer', '-o','local', music_file], preexec_fn=os.setsid)
                                        proc_music_on = True
                                        print "Process: ", proc_music.pid, os.getpgid(proc_music.pid)
                        else:
                                if (proc_music_on == True):
                                        proc_music_on = False
                                        print "Stopping Music..", proc_music.pid
                                        os.killpg(os.getpgid(proc_music.pid), signal.SIGINT)
                        ReedCount = 0
        except KeyboardInterrupt:
                destroy()

