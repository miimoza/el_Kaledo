import subprocess
import importlib
import el_kaledo

while True:
	subprocess.check_call(["git","pull"])
	importlib.reload(el_kaledo)
	el_kaledo.main()
