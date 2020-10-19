import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
GPIO.setup(4,GPIO.IN)

try:
    while 1:
        if (GPIO.input(18) == GPIO.HIGH) or (GPIO.input(4) == GPIO.HIGH):
            subprocess.call("aplay /home/pi/Music/family.wav", shell=True)
            #subprocess.call("omxplayer -o local /home/pi/Videos/family.mp4", shell=True)
            time.sleep(3)
            
except KeyboardInterrupt:
    print("STOP")
    
finally:
    GPIO.cleanup()