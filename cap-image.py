import time
import picamera as cam

with cam.PiCamera() as camera:
	try:
		camera.resolution = (1024, 768)
		while True:
			camera.start_preview()
			time.sleep(2)
	except KeyboardInterrupt:
		camera.capture('image.jpg')
		camera.stop_preview()
