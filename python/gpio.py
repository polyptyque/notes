import RPi.GPIO as GPIO       							  ## Import GPIO Library
import time                   							  ## Import 'time' library (for 'sleep')
 
pin = 7                         						  ## We're working with pin 4
GPIO.setmode(GPIO.BOARD)        						  ## Use BOARD pin numbering


GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)        ## Set pin 4 to INPUT

waiting = True

def my_callback(channel): 
    waiting = False 
    print "falling edge detected"
    #exit() 

GPIO.add_event_detect(pin, GPIO.RISING, callback=my_callback)

while True :
    time.sleep(1)