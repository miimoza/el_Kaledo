from multiprocessing import Process
import RPi.GPIO as GPIO
import schedule
from datetime import datetime
import os
import threading

def switch(pin, t):
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.HIGH)

    threading.Timer(t, GPIO.setup, [pin, GPIO.IN]).start()

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

    schedule_list = [
        ["14:00", SWITCH_OXYGENTANK, 600, "OXYGEN"],
		["15:00", SWITCH_WATERPUMP, 60, "WATER PUMP"],
        ["16:00", SWITCH_OXYGENTANK, 600, "OXYGEN"],
		["17:00", SWITCH_WATERPUMP, 60, "WATER PUMP"],
        ["18:00", SWITCH_OXYGENTANK, 600, "OXYGEN"],
		["19:00", SWITCH_WATERPUMP, 60, "WATER PUMP"],
        ["20:00", SWITCH_OXYGENTANK, 600, "OXYGEN"],
		["21:00", SWITCH_WATERPUMP, 60, "WATER PUMP"],
		["22:00", SWITCH_OXYGENTANK, 6, "OXYGEN"]
    ]

    return schedule_list

def dump_GUI(schedule_list):
    os.system("clear")
    print("="*29 + "[" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*29)
    print ("EL K-RE D0 v0.1.2".center(78))
    print ("="*75 + "(  )=")
    print("TIME".center(7) + "|" + "GPIO N°".center(9) + "|" + "DURATION (SEC)".center(16) + "|" + "LABEL".center(45))
    print("--------------------------------------------------------------------------------")
    for sched in schedule_list:
        print(sched[0].center(7) +"|"+ str(sched[1]).center(9) +"|"+ str(sched[2]).center(16) +"|"+ sched[3].center(45))
    print ("="*80)
