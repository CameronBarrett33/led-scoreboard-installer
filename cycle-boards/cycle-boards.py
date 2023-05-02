from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)

cycle_button = 21
GND_pin = 19

GPIO.setup(GND_pin, GPIO.OUT) # pull_up_down=GPIO.PUD_DOWN)
GPIO.output(GND_pin, GPIO.LOW)
GPIO.setup(cycle_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
        GPIO.wait_for_edge(cycle_button, GPIO.FALLING, bouncetime=1000)
        sleep(.25)
        if(GPIO.input(cycle_button)==0):
                print("cycle")
                subprocess.call("./cycle-boards.sh")


