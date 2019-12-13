#!/usr/bin/python3

import subprocess
import importlib
import el_kaledo
import schedule
import threading

def main():
        subprocess.check_call(["git","pull"])
        importlib.reload(el_kaledo)
        schedule_list = el_kaledo.set_schedule()
        el_kaledo.apply_schedule(schedule_list)
        el_kaledo.dump_GUI(schedule_list)
        schedule.run_pending()
        threading.Timer(30, main).start()
