#Include the library files
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Delay time
delay = 0.07

#Set the LED pins as output pins
for x in range(2,10):
    GPIO.setup(x,GPIO.OUT)
 
#Pattern one
def patternOne(times):
    for a in range (0,times):
        for i in range(2,10):
           GPIO.output(i,GPIO.HIGH)
           sleep(delay)
           GPIO.output(i,GPIO.LOW)

#Pattern two
def patternTwo(times):
    for a in range(0,times):
        for i in range(2,10):
            GPIO.output(i,GPIO.HIGH)
            sleep(delay)
            GPIO.output(i,GPIO.LOW)
            
        for x in range(8,2,-1):
            GPIO.output(x,GPIO.HIGH)
            sleep(delay)
            GPIO.output(x,GPIO.LOW)

#Pattern three
def patternThree(times):
    for a in range(0,times):
        for i in range(2,10):
            GPIO.output(i,GPIO.LOW)
            sleep(delay)
            GPIO.output(i,GPIO.HIGH)
            
        for x in range(8,2,-1):
            GPIO.output(x,GPIO.LOW)
            sleep(delay)
            GPIO.output(x,GPIO.HIGH)

#Pattern four
def patternFour(times):
    for a in range(0,times):
        for i in range(2,10):
            GPIO.output(i,GPIO.HIGH)
            sleep(delay)       
            
        for x in range(9,2,-1):
            GPIO.output(x,GPIO.LOW)
            sleep(delay)       

#Pattern five
def patternFive(times):
    for a in range(0,times):
        for i in range(2,9):
            GPIO.output(i,GPIO.LOW)
            sleep(delay)       
            
        for x in range(9,1,-1):
            GPIO.output(x,GPIO.HIGH)
            sleep(delay)

#Pattern six
def patternSix(times):
    for a in range(0,times):
        for i in range(2,9):
            GPIO.output(i,GPIO.HIGH)
            GPIO.output(i+1,GPIO.HIGH)
            sleep(delay)
            GPIO.output(i,GPIO.LOW)
            GPIO.output(i+1,GPIO.LOW)
            
        for x in range(8,2,-1):
            GPIO.output(x,GPIO.HIGH)
            GPIO.output(x-1,GPIO.HIGH)
            sleep(delay)
            GPIO.output(x,GPIO.LOW)
            GPIO.output(x-1,GPIO.LOW)
    
while True:
    patternOne(3)
    patternTwo(3)
    patternThree(3)
    patternFour(3)
    patternFive(3)
    patternSix(3)