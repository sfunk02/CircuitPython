# Engineering 3: CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)

## Hello_CircuitPython (ledShift)
For this assignment, I coded with circuit python on Mu and made the neopixel on my Metro express shift colors.

### Code

[LED Shift](ledShift.py)

### Evidence



### Wiring

N/A, plug Metro into PC via USB.

### Reflection
* learning syntax different from Arduino - I had to get used to writing code differently than I did last year. For example, there are no semicolons at the end of phrases in Circuit Python.
* not getting ahead of myself - I found that it was best to start simple when learning a new coding language.
* troubleshooting errors on the Metro Express - The Metro Express was indicating that it had an error by flashing the Neopixel, so I had to look in the serial monitor to figure out what the problem was and fix it.


## CircuitPython_Servo
For this assignment, I coded with circuit python on Mu and made a 180 degree servo sweep back and forth.

### Code

[Servo Sweep](servo.py)
```python
##TLDR
while True:
    myServo.angle = 0 ##Sets servo angle
    time.sleep(1)     ##Waits one second
    myServo.angle = 180
    time.sleep(1)
```
### Evidence



### Wiring

(img src="Images/servoCircuit.png" alt="ServoCircuit" width="200" height="100")

### Reflection
The assignment was relatively straightforward, but the only unintuitive aspect was making sure to add the servo.mpy file from the adafruit_motor folder. This file had to go in the lib folder in the Metro, and the library had to be added at the beginnig of the code. 
