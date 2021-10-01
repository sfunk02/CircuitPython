import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

touch_pad = board.A1
touch = touchio.TouchIn(touch_pad)
touch_pad2 = board.A5
touch2 = touchio.TouchIn(touch_pad2)

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

a = 0
b = 0
c = 0
d = 0

while True:
    if touch.value and a == 0 and c == 0:
        lcd.clear()
        a += 1
        lcd.print(str(b))
        lcd.print("\nUp")
    elif touch.value and a == 1 and c == 0:
        lcd.clear()
        a -= 1
        lcd.print(str(b))
        lcd.print("\nDown")
    c = touch.value
    if touch2.value and a == 1 and d == 0:
        lcd.clear()
        b += 1
        lcd.print(str(b))
        lcd.print("\nUp")
    elif touch2.value and a == 0 and d == 0:
        lcd.clear()
        b -= 1
        lcd.print(str(b))
        lcd.print("\nDown")
    d = touch2.value

