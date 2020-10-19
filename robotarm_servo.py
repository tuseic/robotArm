import RPi.GPIO as GPIO
import time 
"""
GPIO23 --> 2nd morter
GPIO24 --> 1st morter
GPIO25 --> 3rd morter
GPIO5 --> 4th morter
GPIO6 --> 5th morter
GPIO13 --> 6th morter
"""



GPIO.setmode(GPIO.BCM)

gp_out = 23
GPIO.setup(gp_out, GPIO.OUT)

servo = GPIO.PWM(gp_out, 50)
servo.start(0)

for i in range(3):
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    
    servo.ChangeDutyCycle(10.0)
    time.sleep(0.5)
    
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

servo.stop()
GPIO.cleanup()


