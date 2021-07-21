import utime
from machine import Pin
from machine import PWM
import MAX6675

SCK0 = Pin(18, Pin.OUT)
CS0  = Pin(21, Pin.OUT)
SO0  = Pin(20, Pin.IN)

light = Pin(2, Pin.OUT)
fan = Pin(3, Pin.OUT)
heater_upper = Pin(4, Pin.OUT)
heater_lower = Pin(5, Pin.OUT)

light.value(0)
fan.value(0)
heater_upper.value(1)
heater_lower.value(1)




t0 = MAX6675.MAX6675(SCK0, CS0, SO0)

while(True):
    print(t0.read())
    utime.sleep(1)


