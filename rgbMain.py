import time
import board
from rgb import RGB

r1 = board.D8
g1 = board.D9
b1 = board.D10
r2 = board.D4
g2 = board.D5
b2 = board.D7

full = 65535
half = int(65535/2)
fast = 0.5
slow = 2

myRGBled1 = RGB(r1, g1, b1)
myRGBled2 = RGB(r2, g2, b2)


while True:
    '''Shines two RGB LEDs in opposing colors, then rainbows!'''
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.green()
    myRGBled2.magenta()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.Blinky(fast) #higher rate is slower
    myRGBled2.Blinky(fast)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.rainbow()
    myRGBled2.rainbow()
    time.sleep(1)
