from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)

cycle_button = 21
GND_pin = 19

GPIO.setup(GND_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(cycle_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
      if GPIO.input(cycle_button)==0:
            subprocess.call("./cycle-boards.sh")
            sleep(.1)
