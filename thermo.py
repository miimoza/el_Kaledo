import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(20, GPIO.IN)


print("GPIO23:" + str(GPIO.input(20)))
print("GPIO24:" + str(GPIO.input(18)))
