import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.1

while True:

    red = range(0, 255)
    green = range(0, 255)
    blue = range(0, 255)

    for r in red:
        led.fill((r, 100, 100))
        time.sleep(.01)
    for g in green:
        led.fill((100, g, 100))
        time.sleep(.01)
    for b in blue:
        led.fill((100, 100, b))
        time.sleep(.01)

