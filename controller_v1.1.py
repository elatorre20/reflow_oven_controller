import utime
from machine import Pin
from machine import PWM
import MAX6675

SCK0 = Pin(18, Pin.OUT)
CS0  = Pin(21, Pin.OUT)
SO0  = Pin(20, Pin.IN)

t0 = MAX6675.MAX6675(SCK0, CS0, SO0)

light = Pin(2, Pin.OUT)
fan = Pin(3, Pin.OUT)
heater_upper = Pin(4, Pin.OUT)
heater_lower = Pin(5, Pin.OUT)

light.value(1)
fan.value(1)
heater_upper.value(1)
heater_lower.value(1)

def bake(target = 150, time = 5):
    #heats the oven to target,
    #modulates the heating elements to retain that temperature,
    #and cools the oven down after maintaing for time seconds.
    
    ctemp = t0.read()
    while(ctemp < target):
        heater_upper.value(0)
        heater_lower.value(0)
        fan.value(0)
        if(ctemp > 50):
            light.value(0)
        ctemp = t0.read()
        utime.sleep_ms(100)
    deadline = ticks_add(time.ticks_ms(), time*1000)
    while(ticks_diff(deadline, time.ticks_ms()) > 0):
        light.value(0)
        fan.value(0)
        ctemp = t0.read()
        if( ctemp > target):
            heater_upper.value(1)
            heater_lower.value(1)
        elif(ctemp < target):
            heater_upper.value(0)
            heater_lower.value(0)
        time.sleep_ms(500)
    while(ctemp > 50):
        heater_upper.value(1)
        heater_lower.value(1)
        fan.value(0)
        light.value(0)
        ctemp = t0.read()
        utime.sleep_ms(100)
    light.value(1)
    fan.value(1)
    heater_upper.value(1)
    heater_lower.value(1)
    

