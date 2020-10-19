import RPi.GPIO as GPIO
import time
import sys
import termios
import tty

GPIO_list =[0, 24, 23, 25, 5, 13, 6]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_list, GPIO.OUT)

servo1 = GPIO.PWM(GPIO_list[1], 50)
servo2 = GPIO.PWM(GPIO_list[2], 50)
servo3 = GPIO.PWM(GPIO_list[3], 50)
servo4 = GPIO.PWM(GPIO_list[4], 50)
servo5 = GPIO.PWM(GPIO_list[5], 50)
servo6 = GPIO.PWM(GPIO_list[6], 50)

jiku = [0, 6.25, 7.8, 6.34, 5.8, 4.4, 8.4]
jiku_up_limit = [0, ]
jiku_down_limit = [0, ]

servo1.start(jiku[1])
servo2.start(jiku[2])
servo3.start(jiku[3])
servo4.start(jiku[4])
servo5.start(jiku[5])
servo6.start(jiku[6])

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)

def count_plus(i):
    if jiku[i] < 10.0:
        jiku[i] += 0.1
    
def count_minus(i):
    if i == 6:
        if jiku[6] > 2.5:
            jiku[6] -= 0.1
    else:
        if jiku[i] > 2.5:
            jiku[i] -= 0.1
        

try:
    while(True):
        tty.setcbreak(sys.stdin.fileno())
        char = sys.stdin.read(1)
        #Left and right movement
        if char == 'a':
            jiku = [0, 6.25, 7.8, 6.34, 5.8, 4.4, 8.4]
            servo1.ChangeDutyCycle(jiku[1])
            servo2.ChangeDutyCycle(jiku[2])
            servo3.ChangeDutyCycle(jiku[3])
            servo4.ChangeDutyCycle(jiku[4])
            servo5.ChangeDutyCycle(jiku[5])
            servo6.ChangeDutyCycle(jiku[6])
        elif char == 'z':
            count_plus(1)
            servo1.ChangeDutyCycle(jiku[1])
        elif char == 'q':
            count_minus(1)
            servo1.ChangeDutyCycle(jiku[1])
        elif char == 'w':
            count_plus(2)
            servo2.ChangeDutyCycle(jiku[2])
        elif char == 'x':
            count_minus(2)
            servo2.ChangeDutyCycle(jiku[2])
        elif char == 'e':
            count_plus(3)
            servo3.ChangeDutyCycle(jiku[3])
        elif char == 'c':
            count_minus(3)
            servo3.ChangeDutyCycle(jiku[3])
        elif char == 'v':
            count_plus(4)
            servo4.ChangeDutyCycle(jiku[4])
        elif char == 'r':
            count_minus(4)
            servo4.ChangeDutyCycle(jiku[4])
        elif char == 't':
            count_plus(5)
            servo5.ChangeDutyCycle(jiku[5])
        elif char == 'b':
            count_minus(5)
            servo5.ChangeDutyCycle(jiku[5])
        elif char == 'y':
            count_plus(6)
            servo6.ChangeDutyCycle(jiku[6])
        elif char == 'n':
            count_minus(6)
            servo6.ChangeDutyCycle(jiku[6])
        elif char == 'A':
            print("ue")
            count_minus(2)
            servo2.ChangeDutyCycle(jiku[2])
        elif char == 'B':
            print("sita")
            count_plus(2)
            servo2.ChangeDutyCycle(jiku[2])
        elif char == 'C':
            print("right")
            count_minus(1)
            servo1.ChangeDutyCycle(jiku[1])
        elif char == 'D':
            print("left")
            count_plus(1)
            servo1.ChangeDutyCycle(jiku[1])
        elif char == '.':
            count_plus(6)
            servo6.ChangeDutyCycle(jiku[6])
        elif char == '0':
            count_minus(6)
            servo6.ChangeDutyCycle(jiku[6])
            
        
        # else:
            # print("Warning:please input fixed commands.")
        
        print(char)
        time.sleep(0.01)
  

except KeyboardInterrupt:
    print("\nSTOP!")
    
finally:
    jiku = [0, 6.25, 7.8, 6.34, 5.8, 4.4, 8.4]
    servo1.ChangeDutyCycle(jiku[1])
    servo2.ChangeDutyCycle(jiku[2])
    servo3.ChangeDutyCycle(jiku[3])
    servo4.ChangeDutyCycle(jiku[4])
    servo5.ChangeDutyCycle(jiku[5])
    time.sleep(0.5)
    servo6.ChangeDutyCycle(jiku[6])
    jiku = [0, 6.15, 4.4, 2.44, 8.0, 4.4, 10.0]
    servo1.ChangeDutyCycle(jiku[1])
    time.sleep(0.5)
    servo2.ChangeDutyCycle(jiku[2])
    time.sleep(0.5)
    servo3.ChangeDutyCycle(jiku[3])
    time.sleep(0.5)
    servo4.ChangeDutyCycle(jiku[4])
    time.sleep(0.5)
    servo5.ChangeDutyCycle(jiku[5])
    time.sleep(0.5)
    servo6.ChangeDutyCycle(jiku[6])
    time.sleep(0.5)
    termios.tcsetattr(fd, termios.TCSANOW, old)        
    print("RESET GPIO & SERVO")
    servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
    servo5.stop()
    servo6.stop()
    GPIO.cleanup()
