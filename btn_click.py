import RPi.GPIO as gpio
import time
import threading

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
    global state
    while True:
        if state:
            gpio.output(17, gpio.HIGH)
            time.sleep(0.1)
            gpio.output(17, gpio.LOW)
            time.sleep(0.1)
                
            gpio.output(22, gpio.HIGH)
            time.sleep(0.1)
            gpio.output(22, gpio.LOW)
            time.sleep(0.1)
        else :
            gpio.output(22, gpio.LOW)
            gpio.output(17, gpio.LOW)

if __name__ == "__main__":
    threading.Thread(target=blink, daemon=True).start()

    while True:
        start = gpio.input(button)
        time.sleep(0.2)
        if start == gpio.HIGH:
            state = not state

