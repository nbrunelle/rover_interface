import keyboard
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# PIN SETUP
GPIO.setup(22,GPIO.OUT) # BACK/FORW
GPIO.setup(4,GPIO.OUT) # LEFT
GPIO.setup(27,GPIO.OUT) # MOTOR
GPIO.setup(26,GPIO.OUT) # MOTOR

def engine():
    print ('activate engine')
    GPIO.output(27,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(27,GPIO.LOW)

def forward():
    print ('trigger forward')
    GPIO.output(22,GPIO.HIGH)
    
def backward():
    print('trigger backward')
    GPIO.output(22,GPIO.LOW)

def left():
    print('move left')
    GPIO.output(4,GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(4,GPIO.LOW)

def right():
    print('move right')
    GPIO.output(26,GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(26,GPIO.LOW)

keyboard.on_press_key('z', lambda _:
        engine()
    )
keyboard.on_press_key('a', lambda _:
        forward()
    )
keyboard.on_press_key('e', lambda _:
        backward()
    )
keyboard.on_press_key('q', lambda _:
        left()
    )
keyboard.on_press_key('d', lambda _:
        right()
    )

keyboard.wait('esc')
keyboard.unhook_all()
print('closing')