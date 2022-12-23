import time
from subprocess import call
import board
from digitalio import DigitalInOut, Direction, Pull

#Requires Adafruit-Blinka module

#Shutdown Raspberry Pi on button press
#Uses button on Adafruit Voice Bonnet
#Meant to run concurrently with main program

button = DigitalInOut(board.D17)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:
  if not button.value:
    print("Shutting down")
    call("sudo shutdown -h now", shell=True)
  time.sleep(0.01)