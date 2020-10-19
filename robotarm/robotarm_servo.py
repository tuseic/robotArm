import RPi.GPIO as GPIO
import time 

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


