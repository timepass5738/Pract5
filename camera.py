from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview() #start camera
sleep(5)
camera.capture(&#39;/home/pi/Desktop/image.jpg&#39;) # take a picture
camera.stop_preview()
