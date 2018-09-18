'''
Created on Sep 13, 2018

@author: JKA
'''

from tkinter import * 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
def distance():
    pass
root = Tk()
root.title("Autobraking System")
root.geometry("540x450+200+200")


button = Button(root, text='Stop', width=50, command=root.destroy)
button.pack()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
TRIGPIN = 11
ECHO = 15 

GPIO.setup(TRIGPIN,GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)


mainloop()

GPIO.output(TRIGPIN, False)
print ("Delay for sensor stability")
time.sleep(2)
GPIO.output(TRIGPIN, True)
time.sleep(0.00001)
GPIO.output(TRIGPIN, False)
while GPIO.input(ECHO)==0:
    pulse_start= 0
    pulse_start= time.time()
while GPIO.input(ECHO)==1:
    pulse_end= 0
    pulse_end= time.time()
duration = pulse_end-pulse_start

distance = duration * 34029
distance = distance / 2
distance = round(distance, 2) 
print ("Distance:",distance,"cm")