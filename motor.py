"""from gpiozero import Motor
motor1 = Motor(3, 4)
motor2 = Motor(17, 27)
motor1.forward()
motor2.backward()
GPIO.output(motor1,GPIO.LOW)
GPIO.output(motor2,GPIO.LOW)"""

from gpiozero import Motor
import time
motor1 = Motor(3, 4)
motor2 = Motor(17, 27)

while(True):
    command = input("enter command : ")
    if command == "f":
        
        motor1.forward()
        motor2.forward()
        time.sleep(0.3)
        motor1.stop()
        motor2.stop()
    elif command == "b":
        motor1.backward() 
        motor2.backward() 
        time.sleep(0.3)
        motor1.stop()
        motor2.stop()
  
    elif command == "r":
        motor1.forward()
        motor2.stop()
        time.sleep(0.3)
        motor1.stop()
    
    elif command == "l":
        motor2.forward()
        motor1.stop()
        time.sleep(0.3)
        motor2.stop()
    elif command == "re":
        motor1.forward()
        motor2.backward() 
        time.sleep(0.4)
        motor1.stop()
        motor2.stop()
    elif command == "er":
        motor1.backward()
        motor2.forward() 
        time.sleep(0.4)
        motor1.stop()
        motor2.stop() 

