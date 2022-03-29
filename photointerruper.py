# Code credit to https://github.com/gventre04/CircuitPython

from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0
interval = 4        # sets interal between each print in seconds

photo = False
state = False

max = interval
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
        counter += 1             # counts each time the photointerrupter is interrupted
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))  # prints counter value
        max = time.time() + interval
        counter = 0
