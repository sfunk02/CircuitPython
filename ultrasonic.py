import board
import time
import neopixel
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.1


while True:
    try:
        print((sonar.distance,))

        if sonar.distance < 5:
            led.fill((255, 0, 0))

        if sonar.distance >= 5 and sonar.distance < 20:
            blue = simpleio.map_range(sonar.distance, 5, 20, 0, 255)
            red = simpleio.map_range(sonar.distance, 5, 20, 255, 0)
            r = int(red)
            b = int(blue)
            led.fill((r, 0, b))
            print((red, blue))

        if sonar.distance >= 20 and sonar.distance < 35:
            green = simpleio.map_range(sonar.distance, 20, 35, 0, 255)
            blue = simpleio.map_range(sonar.distance, 20, 35, 255, 0)
            g = int(green)
            b = int(blue)
            led.fill((0, g, b))

        if sonar.distance >= 35:
            led.fill((0, 255, 0))

    except RuntimeError:
        print("Retrying!")

    time.sleep(.1)
