from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)

cycle_button = 21
GND_pin = 19

GPIO.setup(GND_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(cycle_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
current_state = GPIO.input(GND_pin)

while(1):
      GPIO.wait_for_edge(cycle_button, GPIO.BOTH, bouncetime=200)
      print("cycle")
      subprocess.call("./cycle-boards.sh")
