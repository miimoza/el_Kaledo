import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


while True:
	GPIO.setup(1, GPIO.OUT)
	GPIO.output(1, GPIO.LOW)
	time.sleep(3)
	GPIO.setup(1, GPIO.IN)
	GPIO.output(1, GPIO.HIGH)
