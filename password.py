import RPi.GPIO as gpio
import time
import threading

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(26, gpio.OUT)
gpio.output(26, gpio.LOW)

button1 = 17
gpio.setup(button1, gpio.IN, pull_up_down=gpio.PUD_DOWN)

button2 = 22
gpio.setup(button2, gpio.IN, pull_up_down=gpio.PUD_DOWN)

button3 = 27
gpio.setup(button3, gpio.IN, pull_up_down=gpio.PUD_DOWN)

openState = True

password = [3, 1, 2]
input_sequence = []
timer = None

def lock():
    global input_sequence
    input_sequence.clear()  
    print("잠금")
    while openState:
        gpio.output(26, gpio.HIGH)
        time.sleep(0.1)
        gpio.output(26, gpio.LOW)
        time.sleep(0.1)  

def open():
    print("열림")
    gpio.output(26, gpio.HIGH)

def handle_button_press(button):
    if button == button1:
        input_sequence.append(1)
    elif button == button2:
        input_sequence.append(2)
    elif button == button3:
        input_sequence.append(3)
    print(input_sequence)

    

def button_gogo():
    while len(input_sequence) < 3:
        if gpio.input(button1) == gpio.HIGH:
            handle_button_press(button1)
            time.sleep(0.3)
        if gpio.input(button2) == gpio.HIGH:
            handle_button_press(button2)
            time.sleep(0.3)
        if gpio.input(button3) == gpio.HIGH:
            handle_button_press(button3)
            time.sleep(0.3)
    if len(input_sequence) == 3:
        check()

def check():
    global input_sequence
    if input_sequence == password :
        open()
    else:
        lock()       

button_gogo()
# open()



















