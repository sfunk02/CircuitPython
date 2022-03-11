import time
import pwmio

class LED:

    def __init__(self, r, g, b):
        self.r = pwmio.PWMOut(r, frequency=5000, duty_cycle=65535)
        self.g = pwmio.PWMOut(g, frequency=5000, duty_cycle=65535)
        self.b = pwmio.PWMOut(b, frequency=5000, duty_cycle=65535)

    def fade(self):
        for i in range(65535, 20000, -10):
            self.r.duty_cycle = i
        for i in range(20000, 65535, 10):
            self.r.duty_cycle = i
        for j in range(65535, 20000, -10):
            self.g.duty_cycle = j
        for j in range(20000, 65535, 10):
            self.g.duty_cycle = j
        for k in range(65535, 20000, -10):
            self.b.duty_cycle = k
        for k in range(20000, 65535, 10):
            self.b.duty_cycle = k

    def off(self):
        self.r.duty_cycle = int(65535)
        self.g.duty_cycle = int(65535)
        self.b.duty_cycle = int(65535)
