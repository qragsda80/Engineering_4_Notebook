import adafruit_mpu6050
import busio
import time
import board
import digitalio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led1 = digitalio.DigitalInOut(board.GP16)
led1.direction = digitalio.Direction.OUTPUT


while True:
    print(f"x = {mpu.acceleration[0]}, y = {mpu.acceleration[1]}, z = {mpu.acceleration[2]}")
    time.sleep (.1) 
    if abs(mpu.acceleration[0]) >= 9 or abs(mpu.acceleration[1]) >= 9:
        led1.value = True
    else:
        led1.value = False
#If the acceleration for any axis is greater than or equal to 9, turn on the LED
    
