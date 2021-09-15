import time
import board
import pulseio
import servo

pwm = pulseio.PWMOut(board.D8, frequency=50)

myServo = servo.Servo(pwm, min_pulse=750, max_pulse=2250)

while True:
    myServo.angle = 0
    time.sleep(1)
    myServo.angle = 180
    time.sleep(1)
