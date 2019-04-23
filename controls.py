import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

gpio.cleanup()
tf = 3

def reset():
    Rf.ChangeDutyCycle(0)
    Rb.ChangeDutyCycle(0)    
    Lf.ChangeDutyCycle(0)
    Lb.ChangeDutyCycle(0) 
    

#function moves vehicles forward
def forward(): #tf --> how long does function run
    #Left motor
    print("Going forward")
    for i in range(100):
        Lf.ChangeDutyCycle(i)
        Rf.ChangeDutyCycle(i)
        time.sleep(0.02)

    Lf.ChangeDutyCycle(100)
    Rf.ChangeDutyCycle(100)
    time.sleep(tf)
    print("forward")
        
    for i in range(100):
        Lf.ChangeDutyCycle(100-i)
        Rf.ChangeDutyCycle(100-i)
        time.sleep(0.02)
    print("Done")
    reset()


#function moves vehicles backward
def reverse(): #tf --> how long does function run
    print("Going Backward")

    for i in range(100):
        Lb.ChangeDutyCycle(i)
        Rb.ChangeDutyCycle(i)
        time.sleep(0.02)
    
    Lb.ChangeDutyCycle(100)
    Rb.ChangeDutyCycle(100)
    time.sleep(tf)
        
    for i in range(100):
        Lb.ChangeDutyCycle(100-i)
        Rb.ChangeDutyCycle(100-i)
        time.sleep(0.02)
    print("Done")
    
    Lb.ChangeDutyCycle(0)
    Rb.ChangeDutyCycle(0)
    reset()

 #function turns vehicles to left
def turn_left(): #tf --> how long does function run
    print("Turning left")
    for i in range(100):
        Rf.ChangeDutyCycle(i)
        Lb.ChangeDutyCycle(i)
        time.sleep(0.02)
     
    Rf.ChangeDutyCycle(100)
    Lb.ChangeDutyCycle(100)
    time.sleep(tf)
     
    for i in range(100):
        Rf.ChangeDutyCycle(100-i)
        Lb.ChangeDutyCycle(100-i)
        time.sleep(0.02)   
    print("Done")
    Rf.ChangeDutyCycle(0)
    Lb.ChangeDutyCycle(0)

#function turns vehicles right
def turn_right(): #tf --> how long does function run
    print("Turning Right")

    for i in range(100):
        Lf.ChangeDutyCycle(i)
        Rb.ChangeDutyCycle(i)
        time.sleep(0.02)
        
    Lf.ChangeDutyCycle(100)
    Rb.ChangeDutyCycle(100)
    time.sleep(tf)        
        
    for i in range(100):
        Lf.ChangeDutyCycle(100-i)
        Rb.ChangeDutyCycle(100-i)
        time.sleep(0.02)
    
    print("Done")
    Lf.ChangeDutyCycle(0)
    Rb.ChangeDutyCycle(0)
    reset()

#notifies user if he or she has entered an invalid key. Prevents motors from turning on
def try_again():
    print("Invalid command. Please enter 'W', 'S', 'A', or 'D' to control vehicle")
    Rf.ChangeDutyCycle(0)
    reset()    
 
 #Reads user key input
def key_input(event):
    #reset()
    print 'Key:' , event.char
    key_press = event.char
    
    #'w' key moves vehicle foward
    if key_press.lower() == 'w':
        forward()
    #'s' key moves vehicle backward
    elif key_press.lower() == 's':
        reverse()
    #'a' key turns vehicle to left
    elif key_press.lower() == 'a':
        turn_left()
        
    #'d' key turns vehicle to right
    elif key_press.lower() == 'd':
        turn_right()
    else:
        try_again()

#main program
#Function sets up GPIO pins
gpio.setmode(gpio.BOARD)
    #Left motor
gpio.setup(35, gpio.OUT)
gpio.setup(37, gpio.OUT)
    #Right motor
gpio.setup(36, gpio.OUT)
gpio.setup(38, gpio.OUT)
    
Lf = gpio.PWM(35,1000)
Lb = gpio.PWM(37,1000)
Rf = gpio.PWM(38,1000)
Rb = gpio.PWM(36,1000)
    
Lf.start(0)
Lb.start(0)
Rf.start(0)
Rb.start(0)
print("Commands: Forward: W ; Backward: S ; Right: D ; Left: A")
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
    

