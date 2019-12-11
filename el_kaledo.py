import RPi.GPIO as GPIO
import time


def switch_on(pin, t, gpio_out):
	if gpio_out:
		GPIO.setup(pin, GPIO.OUT)
	else:
		GPIO.setup(pin, GPIO.IN)

	GPIO.output(pin, GPIO.LOW)
	time.sleep(t)
	GPIO.output(pin, GPIO.HIGH)

def main():
	SWITCH_WATERPUMP = 1
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14


	GPIO.setmode(GPIO.BCM)


	switch_on(SWITCH_WATERPUMP, 1, 1)
	switch_on(SWITCH_OXYGENTANK, 1, 1)


	GPIO.cleanup()


	time.sleep(2)
