import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BCM) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(23,GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
left_door = GPIO.PWM(23, 50)     # Sets up pin 12 as a PWM pin
left_door.start(0)
GPIO.setup(24,GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
right_door = GPIO.PWM(24, 50)     # Sets up pin 12 as a PWM pin
right_door.start(0)
i=0# Starts running PWM on the pin and sets it to 0
while(i<20):
    door = input("which door you want to operate left/right : ")
    if(door == "l"):
        s = input("door open/close give command in o/c" )
# Move the servo back and forth
        if(s == "o"):
            left_door.ChangeDutyCycle(8)
            # Changes the pulse width to 3 (so moves the servo)
            sleep(0.2)
        elif(s == "c"):
            left_door.ChangeDutyCycle(12)     # Changes the pulse width to 3 (so moves the servo)
            sleep(0.2)
    elif(door == "r"):
        s = input("door open/close give command in o/c" )
# Move the servo back and forth
        if(s == "o"):
            right_door.ChangeDutyCycle(12)     # Changes the pulse width to 3 (so moves the servo)
            sleep(0.2)
        elif(s == "c"):
            right_door.ChangeDutyCycle(6)     # Changes the pulse width to 3 (so moves the servo)
            sleep(0.2)
#p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
#sleep(1) # Wait 1 second
    #p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)come to original position
    #sleep(0.2)
    i = i+1

# Clean up everything
right_door.stop()
left_door.stop()# At the end of the program, stop the PWM
GPIO.cleanup()