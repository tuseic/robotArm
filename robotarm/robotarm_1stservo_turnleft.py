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


"""
GPIO.setmode(GPIO.BCM)

gp_out = 24
GPIO.setup(gp_out, GPIO.OUT)

servo = GPIO.PWM(gp_out, 50)
servo.start(0)
"""

GPIO_list =[0, 24, 23, 25, 5, 6, 13]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_list, GPIO.OUT)

servo1 = GPIO.PWM(GPIO_list[1], 50)
servo2 = GPIO.PWM(GPIO_list[2], 50)
servo3 = GPIO.PWM(GPIO_list[3], 50)
servo4 = GPIO.PWM(GPIO_list[4], 50)
servo5 = GPIO.PWM(GPIO_list[5], 50)
servo6 = GPIO.PWM(GPIO_list[6], 50)

servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)
servo5.start(0)
servo6.start(0)
char = input()

if char == 'a':
    servo1.ChangeDutyCycle(10.0)
    time.sleep(0.5)

servo.stop()
GPIO.cleanup()


