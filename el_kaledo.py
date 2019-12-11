import RPi.GPIO as GPIO
import time


def main():
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(SWITCH_WATERPUMP, GPIO.OUT)
	GPIO.output(SWITCH_WATERPUMP, GPIO.LOW)
	time.sleep(1)
	GPIO.setup(SWITCH_WATERPUMP, GPIO.OUT)
	GPIO.output(SWITCH_WATERPUMP, GPIO.HIGH)



	GPIO.cleanup()


	time.sleep(2)
