import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

gpio.cleanup()
#Function sets up GPIO pins
def init():
    gpio.setmode(gpio.BOARD)
    #Left motor
    gpio.setup(35, gpio.OUT)
    gpio.setup(37, gpio.OUT)
    #Right motor
    gpio.setup(36, gpio.OUT)
    gpio.setup(38, gpio.OUT)

#function moves vehicles forward
def forward(tf): #tf --> how long does function run
    #Left motor
    print("Forward")
    gpio.output(35, True)
    gpio.output(37, False)
    #Right motor
    gpio.output(36, False)
    gpio.output(38, True)
    time.sleep(tf)
    gpio.cleanup()

#function moves vehicles backward
def reverse(tf): #tf --> how long does function run
    print("Reverse")
    #Left motor
    gpio.output(35, False)
    gpio.output(37, True)
    #Left motor
    gpio.output(36, True)
    gpio.output(38, False)
    time.sleep(tf)
    gpio.cleanup()
 
 #function turns vehicles to left
def turn_left(tf): #tf --> how long does function run
    print("Left")
    #Left motor
    gpio.output(35, True)
    gpio.output(37, False)
    #Left motor
    gpio.output(36, True)
    gpio.output(38, False)
    time.sleep(tf)
    gpio.cleanup()

#function turns vehicles right
def turn_right(tf): #tf --> how long does function run
    print("Right")
    #Left motor
    gpio.output(35, False)
    gpio.output(37, True)
    #Left motor
    gpio.output(36, False)
    gpio.output(38, True)
    time.sleep(tf)
    gpio.cleanup()

#notifies user if he or she has entered an invalid key. Prevents motors from turning on
def try_again():
    print("Invalid command. Please enter 'W', 'S', 'A', or 'D' to control vehicle")    #Left motor
    gpio.output(35, False)
    gpio.output(37, False)
    #Left motor
    gpio.output(36, False)
    gpio.output(38, False)
    time.sleep(0)
    gpio.cleanup()
    
 
 #Reads user key input
def key_input(event):
    init()
    print 'Key:' , event.char
    key_press = event.char
    sleep_time = 0.3
    
    #'w' key moves vehicle foward
    if key_press.lower() == 'w':
        forward(sleep_time)
    #'s' key moves vehicle backward
    elif key_press.lower() == 's':
        reverse(sleep_time)
    #'a' key turns vehicle to left
    elif key_press.lower() == 'a':
        turn_left(0.3)
        
    #'d' key turns vehicle to right
    elif key_press.lower() == 'd':
        turn_right(0.3)
    else:
        try_again()
        
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
    

