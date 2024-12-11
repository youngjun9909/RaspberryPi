import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(17, gpio.OUT)
gpio.output(17, gpio.LOW)
gpio.setup(22, gpio.OUT)
gpio.output(22, gpio.LOW)
gpio.setup(27, gpio.OUT)
gpio.output(27, gpio.LOW)

button = 23
gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_DOWN)

state = False


def blink():
    gpio.output(17, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(17, gpio.LOW)
    time.sleep(0.1)
        
    gpio.output(22, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(22, gpio.LOW)
    time.sleep(0.1)

while True:    
    start = gpio.input(button)
    time.sleep(0.1)
    if start == gpio.HIGH:
        state = not state
    if state:
        blink()
    else:
        gpio.output(22, gpio.LOW)
        gpio.output(17, gpio.LOW)