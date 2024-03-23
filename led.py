import gpiozero
from gpiozero import LED
import time
# Define LED pin 
LED_PIN = 18
i = 0
# Create LED object
led = LED(LED_PIN)

while i<3:
# Turn on LED
    led.on()

# Keep LED on for 1 second
    time.sleep(3)

# Turn off LED 
    led.off()
    time.sleep(2)
    i = i+1
    