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


def apply_schedule(schedule_list):
        for sched in schedule_list:
                schedule.every().day.at(sched[0]).do(start_thread, switch, sched[1], sched[2])

        
def set_schedule():
	SWITCH_WATERPUMP = 21
	ALIM5V_WATERPUMP = 4
	GROUND_WATERPUMP = 6

	SWITCH_OXYGENTANK = 20
	ALIM5V_OXYGENTANK = 2
	GROUND_OXYGENTANK = 14

	GPIO.setmode(GPIO.BCM)

        schedule_list = [["14:00", SWICTH_OXYGEN, 600, "OXYGEN"],["16:00", SWITCH_OXYGEN, 600, "OXYGEN"],["18:00", SWITCH_OXYGEN, 600, "OXYGEN"],["20:00", SWITCH_OXYGEN, 600, "OXYGEN"]]
        
        return schedule_list

def dump_GUI(schedule_list):
        os.system("clear")
        print ("=========================[ " + str(datetime.now()) + " ]=========================") 
        print ("EL K-RE D0 v0.1.2") 


 
        print ("===========================================================================(  )=")

        print()
        print("     HOUR     |   GPIO N°   |  TIME (SEC) |    LABEL    ")
        for sched in schedule:
                print(sched[0].ljust(14) + sched[1].ljust(14) + sched[2].ljust(14) + sched[3].ljust(14))
                print(sched[1].ljust(15)

         
