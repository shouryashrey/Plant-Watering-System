import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

activePin = 8

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(activePin, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


def waterPlants(seconds):
 GPIO.output(activePin, GPIO.HIGH) # Turn on
 sleep(seconds) # Sleep for 1 second
 GPIO.output(activePin, GPIO.LOW) # Turn off

def blinkFor(times):
 for i in range(times):
  GPIO.output(activePin, GPIO.HIGH) # Turn on
  sleep(0.2) # Sleep for 1 second
  GPIO.output(activePin, GPIO.LOW) # Turn off
  sleep(0.2) # Sleep for 1 second


def blinkForWithInterval(times, interval=1):
 for i in range(times):
  GPIO.output(activePin, GPIO.HIGH) # Turn on
  sleep(interval) # Sleep for 1 second
  GPIO.output(activePin, GPIO.LOW) # Turn off
  sleep(interval) # Sleep for 1 second


# while True: # Run forever
#  GPIO.output(activePin, GPIO.HIGH) # Turn on
#  sleep(1) # Sleep for 1 second
#  GPIO.output(activePin, GPIO.LOW) # Turn off
#  sleep(1) # Sleep for 1 second