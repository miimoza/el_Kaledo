from multiprocessing import Process
import RPi.GPIO as GPIO
import time
import schedule


def switch(pin, t):
	GPIO.setup(pin, GPIO.OUT)

	GPIO.output(pin, GPIO.HIGH)
	time.sleep(t)

	GPIO.setup(pin, GPIO.IN)

def start_thread(function, pin, time):
	switch_thread = Process(target=switch, args=(pin, time))
	switch_thread.start()

def main():
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14




	GPIO.setmode(GPIO.BCM)


	schedule.every().day.at("04:04").do(start_thread, switch, SWITCH_WATERPUMP, 3)
	schedule.every().day.at("04:05").do(start_thread, switch, SWITCH_WATERPUMP, 3)

	while True:
		schedule.run_pending()
		time.sleep(5) # wait one minute
