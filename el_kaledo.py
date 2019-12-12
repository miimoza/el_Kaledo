from multiprocessing import Process
import RPi.GPIO as GPIO
import schedule
from datetime import datetime
import os

def switch(pin, t):
	GPIO.setup(pin, GPIO.OUT)

	GPIO.output(pin, GPIO.HIGH)
	time.sleep(t)

	GPIO.setup(pin, GPIO.IN)

def start_thread(function, pin, time):
	switch_thread = Process(target=switch, args=(pin, time))
	switch_thread.start()

def set_schedule():
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14

	GPIO.setmode(GPIO.BCM)

	schedule.every().day.at("17:00").do(start_thread, switch, SWITCH_OXYGENTANK, 600)
	schedule.every().day.at("18:00").do(start_thread, switch, SWITCH_OXYGENTANK, 600)
	schedule.every().day.at("19:00").do(start_thread, switch, SWITCH_OXYGENTANK, 600)
	schedule.every().day.at("20:00").do(start_thread, switch, SWITCH_OXYGENTANK, 600)	


def dump_GUI():
        os.system("clear")
        print (datetime.now())
        print ("on est plus que chaud")  
