#Include the library files
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Delay time
delay = 0.07
ledl=[4,21,26,19,13,6]
#Set the LED pins as output pins
for x in ledl:
    GPIO.setup(x,GPIO.OUT)
 
#Pattern one
def patternOne(times):
    
        for i in ledl:
           GPIO.output(i,GPIO.HIGH)
           sleep(delay)
           GPIO.output(i,GPIO.LOW)

#Pattern two
def patternTwo(times):
    
        for i in ledl:
            GPIO.output(i,GPIO.HIGH)
            sleep(delay)
            GPIO.output(i,GPIO.LOW)
            
        for xx in range(len(ledl)):
            x=ledl[len(ledl)-xx-1]
            GPIO.output(x,GPIO.HIGH)
            sleep(delay)
            GPIO.output(x,GPIO.LOW)

#Pattern three
def patternThree(times):
    
        for i in ledl:
            GPIO.output(i,GPIO.LOW)
            sleep(delay)
            GPIO.output(i,GPIO.HIGH)
            
        for xx in range(len(ledl)):
            x=ledl[len(ledl)-xx-1]
            GPIO.output(x,GPIO.LOW)
            sleep(delay)
            GPIO.output(x,GPIO.HIGH)

#Pattern four
def patternFour(times):
    
        for i in ledl:
            GPIO.output(i,GPIO.HIGH)
            sleep(delay)       
            
        for xx in range(len(ledl)):
            x=ledl[len(ledl)-xx-1]
            GPIO.output(x,GPIO.LOW)
            sleep(delay)       

#Pattern five
def patternFive(times):
    
        for i in ledl:
            GPIO.output(i,GPIO.LOW)
            sleep(delay)       
            
        for xx in range(len(ledl)):
            x=ledl[len(ledl)-xx-1]
            GPIO.output(x,GPIO.HIGH)
            sleep(delay)

#Pattern six
def patternSix(times):
    
        for i in ledl:
            GPIO.output(i,GPIO.HIGH)
            GPIO.output(i+1,GPIO.HIGH)
            sleep(delay)
            GPIO.output(i,GPIO.LOW)
            GPIO.output(i+1,GPIO.LOW)
            
        for xx in range(len(ledl)):
            x=ledl[len(ledl)-xx-1]
            GPIO.output(x,GPIO.HIGH)
            GPIO.output(x-1,GPIO.HIGH)
            sleep(delay)
            GPIO.output(x,GPIO.LOW)
            GPIO.output(x-1,GPIO.LOW)

c=0
def runner(c):
    if c<6:
        c+=1
        return c
    else:
        c=0
        return c
    


while True:
    GPIO.add_event_detect(16,GPIO.RISING,callback=runner)
    
    if c==0:
        patternOne(3)
    elif c==1:
        patternTwo(3)
    elif c==2:    
        patternThree(3)
    elif c==3:
        patternFour(3)
    elif c==4:
        patternFive(3)
    elif c==5:    
        patternSix(3)


