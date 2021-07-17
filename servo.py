#import libs
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

#Initiakize PWM 
servo = GPIO.PWM(40,50)
servo.start(0)

 
while True:    
    print("0")
    servo.ChangeDutyCycle(2.5)
    time.sleep(1)
    print("180")
    servo.ChangeDutyCycle(12.5)
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()
    break
        
        


    
