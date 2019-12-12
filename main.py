import subprocess
import importlib
import el_kaledo
import schedule
import time

while True:
        subprocess.check_call(["git","pull"])
        importlib.reload(el_kaledo)
        el_kaledo.set_schedule()
        el_kaledo.dump_GUI()
        schedule.run_pending()
        time.sleep(30)
      
        
