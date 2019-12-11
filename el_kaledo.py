import RPi.GPIO as GPIO
import time


def switch_on(pin, t, gpio_out):
	if gpio_out:
		GPIO.setup(pin, GPIO.OUT)
	else:
		GPIO.setup(pin, GPIO.IN)

	GPIO.output(pin, GPIO.HIGH)
	time.sleep(t)

def main():
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14


	GPIO.setmode(GPIO.BCM)

	GPIO.setup(GROUND_WATERPUMP, GPIO.IN)
	GPIO.setup(ALIM5V_WATERPUMP, GPIO.OUT)
	GPIO.output(ALIM5V_WATERPUMP, GPIO.LOW)
	switch_on(SWITCH_WATERPUMP, 1, 1)
	GPIO.output(ALIM5V_WATERPUMP, GPIO.HIGH)


	switch_on(SWITCH_OXYGENTANK, 1, 1)


	GPIO.cleanup()


	time.sleep(2)
