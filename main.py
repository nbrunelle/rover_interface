# import keyboard
from sshkeyboard import listen_keyboard

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# PIN SETUP
GPIO.setup(22,GPIO.OUT) # BACK/FORW
GPIO.setup(4,GPIO.OUT) # LEFT
GPIO.setup(27,GPIO.OUT) # MOTOR
GPIO.setup(26,GPIO.OUT) # MOTOR

general_secure = True

def engine(secure):
    print ('activate engine')
    GPIO.output(27,GPIO.HIGH)
    if(secure):
        time.sleep(1)
        GPIO.output(27,GPIO.LOW)
def forward():
    print ('trigger forward')
    GPIO.output(22,GPIO.HIGH)
    
def backward():
    print('trigger backward')
    GPIO.output(22,GPIO.LOW)

def left(secure):
    print('move left')
    GPIO.output(4,GPIO.HIGH)
    if(secure):
        time.sleep(.1)
        GPIO.output(4,GPIO.LOW)

def right(secure):
    print('move right')
    GPIO.output(26,GPIO.HIGH)
    if(secure):
        time.sleep(.1)
        GPIO.output(26,GPIO.LOW)
    
def press(key):
    global general_secure
    if(key == '!'):
        if(general_secure == True):
            print ('Unsafe mode activated!!!')
            general_secure = False
        else:
            print('Back to safety')
            general_secure = True
    if(key == 'z'):
        engine(general_secure)
    if(key == 'a'):
        backward()
    if(key == 'e'):
        forward()
    if(key == 'q'):
        left(general_secure)
    if(key == 'd'):
        right(general_secure)
        
def release(key):
    global general_secure
    if(general_secure == False):
        print('Everything stopped')
        GPIO.output(27,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)    

listen_keyboard(
    on_press=press,
    on_release=release
)

print('closing')