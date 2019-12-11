import RPi.GPIO as GPIO
import time


def switch_on(pin, time):
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(time)
	GPIO.output(pin, GPIO.LOW)

def main():
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14



	GPIO.setmode(GPIO.BCM)

	GPIO.setup(SWITCH_WATERPUMP, GPIO.OUT)

	switch_on(SWITCH_WATERPUMP, 1)



	GPIO.cleanup()


	time.sleep(2)
