# Engineering 3: CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)

## Hello_CircuitPython (ledShift)
For this assignment, I coded with circuit python on Mu and made the neopixel on my Metro express shift colors.

### Code
```python
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
```
### Evidence



### Wiring



### Reflection
* learning syntax different from Arduino - I had to get used to writing code differently than I did last year. For example, there are no semicolons at the end of phrases in Circuit Python.
* not getting ahead of myself - I found that it was best to start simple when learning a new coding language.
* troubleshooting errors on the Metro Express - The Metro Express was indicating that it had an error by flashing the Neopixel, so I had to look in the serial monitor to figure out what the problem was and fix it.


## CircuitPython_Servo
For this assignment, I coded with circuit python on Mu and made the neopixel on my Metro express shift colors.

### Code
```python

```
### Evidence



### Wiring



### Reflection
