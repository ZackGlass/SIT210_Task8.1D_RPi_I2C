import RPi.GPIO as GPIO
import adafruit_bh1750
import board
import time

i2c = board.I2C()
sense = adafruit_bh1750.BH1750(i2c)

try:
    while True:
        data = round(sense.lux, 1)
        if data < 51:
            print("Too Dark".ljust(11, " "), "| Lux: ", data)
        elif data > 50 and data < 101:
            print("Dark".ljust(11, " "), "| Lux: ", data)
        elif data > 100 and data < 201:
            print("Medium".ljust(11, " "), "| Lux: ", data)
        elif data > 200 and data < 1001:
            print("Bright".ljust(11, " "), "| Lux: ", data)
        elif data > 1000:
            print("Too Bright".ljust(11, " "), "| Lux: ", data)

        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup       