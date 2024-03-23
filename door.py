import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BCM) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(23,GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
p = GPIO.PWM(23, 50)     # Sets up pin 12 as a PWM pin
p.start(0)
GPIO.setup(24,GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
q = GPIO.PWM(24, 50)     # Sets up pin 12 as a PWM pin
q.start(0)
i=0# Starts running PWM on the pin and sets it to 0
while(i<5):
# Move the servo back and forth
    value = input("which door you want to open L/R : ")
    if value == "l":
        p.ChangeDutyCycle(12)     # Changes the pulse width to 3 (so moves the servo)
        sleep(0.2)
        p.ChangeDutyCycle(6)    # Changes the pulse width to 12 (so moves the servo)come to original position
        sleep(0.2)
    elif value == "r":
        q.ChangeDutyCycle(6)     # Changes the pulse width to 3 (so moves the servo)
        sleep(0.2)
        q.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)come to original position
        sleep(0.2)
    i = i+1

# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()
