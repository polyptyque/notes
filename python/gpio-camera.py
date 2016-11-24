import io
import picamera
import RPi.GPIO as GPIO
import time

# GPIO4 -> pin 7
pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def pressButton(channel):
    t = time.strftime('%Y-%m-%d_%H-%M-%S')
    a = time.clock()
    camera.capture('img-'+t+'.jpg', format='jpeg')
    b = time.clock()
    print 'image shot in '+str(round((b-a)*1000))+'ms '

# enregistre le bouton sur GPIO
GPIO.add_event_detect(pin, GPIO.RISING, callback=pressButton, bouncetime=10)

# declare la camera
camera = picamera.PiCamera()

#stream = io.BytesIO()

# lance la camera
camera.start_preview();
#camera.capture_continuous(stream, format='jpeg')

while True :
     time.sleep(10)