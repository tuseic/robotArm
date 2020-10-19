import RPi.GPIO as GPIO
import time
import sys
import termios
import tty


GPIO_list =[24, 23, 25, 5, 6, 13]
servo = []
jiku = [6.25, 7.8, 6.34, 5.8, 7.05, 4.45]
jiku_key_up = ["q", "z", "w", "x", "e", "c", "r", "v", "t", "b", "y", "n"]
jiku_key_down = ["z", "x", "c", "v", "b", "n"]
        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_list, GPIO.OUT)

for i in range(6):
    servo.append(GPIO.PWM(GPIO_list[i], 50))

for i in range(6):
    servo[i].start(jiku[i])
    
fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)

def count_plus(i):
    if jiku[i] < 10.0:
        jiku[i] += 0.1
    
def count_minus(i):
    if jiku[i] > 2.5:
        jiku[i] -= 0.1
try:
    while(True):
        tty.setcbreak(sys.stdin.fileno())
        char = sys.stdin.read(1)
        for key in range(16):
            
        print(jiku)
        time.sleep(0.01)
  

except KeyboardInterrupt:
    print("\nSTOP!")
    
finally:
    termios.tcsetattr(fd, termios.TCSANOW, old)        
    print("RESET GPIO & SERVO")
    for i in rangej(6):
        servo[i].stop()
    GPIO.cleanup()
