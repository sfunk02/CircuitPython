import time
import pwmio

fadeUp = range(65535, 0, -10)

fadeDown = range(0, 65535, 10)

class RGB:

    def __init__(self, r, g, b):
        self.r = pwmio.PWMOut(r, frequency=5000, duty_cycle=65535)
        self.g = pwmio.PWMOut(g, frequency=5000, duty_cycle=65535)
        self.b = pwmio.PWMOut(b, frequency=5000, duty_cycle=65535)

    def fade(self, brightness=20000):
        for i in range(65535, 65535-brightness, -10):
            self.r.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.r.duty_cycle = i
        for j in range(65535, 65535-brightness, -10):
            self.g.duty_cycle = j
        for j in range(65535-brightness, 65535, 10):
            self.g.duty_cycle = j
        for k in range(65535, 65535-brightness, -10):
            self.b.duty_cycle = k
        for k in range(65535-brightness, 65535, 10):
            self.b.duty_cycle = k

    def blue(self, brightness=20000):
        self.r.duty_cycle = (65535)
        self.g.duty_cycle = (65535)
        self.b.duty_cycle = (65535-brightness)

    def yellow(self, brightness=20000):
        self.r.duty_cycle = (65535-brightness)
        self.g.duty_cycle = (65535-brightness)
        self.b.duty_cycle = (65535)

    def red(self, brightness=20000):
        self.r.duty_cycle = (65535-brightness)
        self.g.duty_cycle = (65535)
        self.b.duty_cycle = (65535)

    def cyan(self, brightness=20000):
        self.r.duty_cycle = (65535)
        self.g.duty_cycle = (65535-brightness)
        self.b.duty_cycle = (65535-brightness)

    def green(self, brightness=20000):
        self.r.duty_cycle = (65535)
        self.g.duty_cycle = (65535-brightness)
        self.b.duty_cycle = (65535)

    def magenta(self, brightness=20000):
        self.r.duty_cycle = (65535-brightness)
        self.g.duty_cycle = (65535)
        self.b.duty_cycle = (65535-brightness)

    def Blinky(self, rate=1, brightness=20000):
        self.red()
        time.sleep(rate)
        self.green()
        time.sleep(rate)
        self.blue()
        time.sleep(rate)

    def rainbow(self, brightness=20000):
        for i in range(65535, 65535-brightness, -10):   # red
            self.r.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.r.duty_cycle = i
        for i in range(65535, 65535-brightness, -10):   # yellow
            self.r.duty_cycle = i
            self.g.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.r.duty_cycle = i
            self.g.duty_cycle = i
        for i in range(65535, 65535-brightness, -10):   # green
            self.g.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.g.duty_cycle = i
        for i in range(65535, 65535-brightness, -10):   # cyan
            self.g.duty_cycle = i
            self.b.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.g.duty_cycle = i
            self.b.duty_cycle = i
        for i in range(65535, 65535-brightness, -10):   # blue
            self.b.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.b.duty_cycle = i
        for i in range(65535, 65535-brightness, -10):   # magenta
            self.r.duty_cycle = i
            self.b.duty_cycle = i
        for i in range(65535-brightness, 65535, 10):
            self.r.duty_cycle = i
            self.b.duty_cycle = i

    def off(self):
        self.r.duty_cycle = (65535)
        self.g.duty_cycle = (65535)
        self.b.duty_cycle = (65535)
