import RPi.GPIO as GPIO
import time
import sys

#Initialize the required IO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#Define methods to move each of the motors 
def clockLeft(x):
   GPIO.output(14,True)
   GPIO.output(15,False)
   time.sleep(x)
def stopLeft():
   GPIO.output(14,False)
   GPIO.output(15,False)
def counterClockLeft(y):
   GPIO.output(15,True)
   GPIO.output(14,False)
   time.sleep(y)
def counterClockRight(z):
   GPIO.output(23,True)
   GPIO.output(24,False)
   time.sleep(z)
def stopRight():
   GPIO.output(23,False)
   GPIO.output(24,False)
def clockRight(a):
   GPIO.output(24,True)
   GPIO.output(23,False)
   time.sleep(a)

#Define methods to move lawnmower in all directions
def forward(b):
   clockLeft(.01) 
   #time.sleep(.0001)
   clockRight(.01)
   time.sleep(b)
   stopLeft()
   stopRight()
def back(c):
   counterClockLeft(.01)
   #time.sleep(.0001)
   counterClockRight(.01)
   time.sleep(c)
   stopLeft()
   stopRight()
def leftTurn(d):
   clockRight(.5)
   time.sleep(d)
   stopRight()
def rightTurn(e):
  clockLeft(.5)
  time.sleep(e)
  stopLeft()

