import time
import board
from rgb import LED

rPin = board.D8
gPin = board.D9
bPin = board.D10

rPin2 = board.D4
gPin2 = board.D5
bPin2 = board.D7

rgbLED = LED(rPin, gPin, bPin)
rgbLED2 = LED(rPin2, gPin2, bPin2)

while True:
    rgbLED.off()
    rgbLED2.off()
    rgbLED.fade()
    rgbLED.off()
    rgbLED2.fade()
    rgbLED2.off()
