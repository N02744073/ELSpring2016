#!ELSpring2016/code/LEDBlink
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def Blink():
	for i in range(0,10):
		blink3= 3
		blink4= 4
		print "blink #" + str(i+1)
		while blink3>0:
			GPIO.output(17,True)
			time.sleep(.2)
			GPIO.output(17,False)
			time.sleep(.2)
			blink3 = blink3 - 1
		time.sleep(5)
		while blink4>0:
			GPIO.output(17,True)
			time.sleep(.2)
			GPIO.output(17,False)
			time.sleep(.2)
			blink4 = blink4 - 1
		time.sleep(5)
	print "done!!"
	GPIO.cleanup()
Blink()
