import machine
import utime
from micropython import const

#constants


class thermocouple_SPI():
    
    def __init__(self, bus, cs):
        self.bus = bus
        self.cs = cs
        self.temp_data = bytearray(2)
        self.cs.value(1)
        
    def select(self):
        self.cs.value(0)
        
    def deselect(self):
        self.cs.value(1)
        
    def read_temp(self):
        self.select()
        self.bus.readinto(self.temp_data)
        return self.temp_data
        