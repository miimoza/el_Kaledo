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
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14


	GPIO.setmode(GPIO.BCM)


	switch_on(SWITCH_WATERPUMP, 0.2, 1)
	GPIO.setup(ALIM5V_WATERPUMP, GPIO.OUT)
	GPIO.output(ALIM5V_WATERPUMP, GPIO.HIGH)
	switch_on(SWITCH_OXYGENTANK, 0.4, 1)

	switch_on(SWITCH_WATERPUMP, 0.1, 1)
	switch_on(SWITCH_WATERPUMP, 0.1, 1)
	switch_on(SWITCH_WATERPUMP, 0.1, 1)


	GPIO.cleanup()


	time.sleep(2)
