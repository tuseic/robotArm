import RPi.GPIO as GPIO
import time
import sys
import termios
import tty

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

"""
char = input()

if char == 'a':
    servo.ChangeDutyCycle(10.0)
    time.sleep(0.5)
"""


try:
    while(True):
        print("please enter the letter.")
        char = input()
        
        #Left and right movement
        if char == 'a2':
            servo1.ChangeDutyCycle(10.0)
            time.sleep(1)
        elif char == 'a':
            servo1.ChangeDutyCycle(7.5)
            time.sleep(1)
        elif char == 'd2':
            servo1.ChangeDutyCycle(2.5)
            time.sleep(1)
        elif char == 'd':
            servo1.ChangeDutyCycle(5.0)
            time.sleep(1)
        elif char == 'ad':
            servo1.ChangeDutyCycle(6.25)
            time.sleep(1)
        
        #Back and forth movement
            #servo2
        elif char == 'w2':
            servo2.ChangeDutyCycle(10.0)
            time.sleep(1)
        elif char == 'w':
            servo2.ChangeDutyCycle(7.5)
            time.sleep(1)
        elif char == 's':
            servo2.ChangeDutyCycle(5.0)
            time.sleep(1)
        elif char == 's2':
            servo2.ChangeDutyCycle(2.5)
            time.sleep(1)
            #servo3
        elif char == 'ww2':
            servo3.ChangeDutyCycle(2.5)
            time.sleep(1)
        elif char == 'ww':
            servo3.ChangeDutyCycle(5.0)
            time.sleep(1)      
        elif char == 'ss2':
            servo3.ChangeDutyCycle(10.0)
            time.sleep(1)
        elif char == 'ss':
            servo3.ChangeDutyCycle(7.5)
            time.sleep(1)
            #servo4
        elif char == 'www2':
            servo4.ChangeDutyCycle(2.5)
            time.sleep(1)
        elif char == 'www':
            servo4.ChangeDutyCycle(5.0)
            time.sleep(1)
        elif char == 'sss2':
            servo4.ChangeDutyCycle(10.0)
            time.sleep(1)
        elif char == 'sss':
            servo4.ChangeDutyCycle(7.5)
            time.sleep(1)
        #Rotate the neck
        elif char == 'ra':
            servo5.ChangeDutyCycle(7.5)
            time.sleep(1)
        elif char == 'rd':
            servo5.ChangeDutyCycle(2.5)
            time.sleep(1)
        #Open and close the hand
        elif char == 'c':
            servo6.ChangeDutyCycle(10.0)
            time.sleep(1)
        elif char == 'o':
            servo6.ChangeDutyCycle(2.5)
            time.sleep(1)
        else:
            print("Warning:please input fixed commands.")
  

except KeyboardInterrupt:
    print("\nSTOP!")

"""
servo.stop()
GPIO.cleanup()
"""
"""    
finally:
    print("RESET GPIO & SERVO")
    servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
    servo5.stop()
    servo6.stop()
    GPIO.cleanup()
"""
print("RESET GPIO & SERVO")
servo1.stop()
servo2.stop()
servo3.stop()
servo4.stop()
servo5.stop()
servo6.stop()
GPIO.cleanup()