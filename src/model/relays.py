import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Relay(object):    
    def __init__(self, pin):
        self.pin = pin
        
    def activate(self):
        GPIO.setup()
