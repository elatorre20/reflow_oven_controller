import machine
import utime
from micropython import const

#constants


class thermocouple_SPI():
    
    def __init__(self, bus, cs):
        self.bus = bus
        self.cs = cs
        self.temp_data = 0
        self.cs.value(1)
        
    def select(self):
        self.cs.value(0)
        
    def deselect(self):
        self.cs.value(1)
        
    def refresh(self):
        self.select()
        utime.sleep_us(10)
        self.deselect()
        
    def read_temp(self):
        #the temperature reading is the 2nd-12th bits (bits 14-3 of the read byte)
        #multiply this number by 0.25 to get the reading in degrees C
        self.select()
        utime.sleep_us(10)
        read = self.bus.read(2)
        self.deselect()
        x = int.from_bytes(read, 'big')
        x = x>>3 #discarding 3 trailing bits
        mask = 0b0111111111111
        y = bin(x) & mask #masking leading zero
        t = 0.25*y
        self.temp_data = t
        return self.temp_data
    
    def get_temp_c(self):
        return(self.read_temp())
        
    def get_temp_k(self):
        return(self.get_temp_c()-273.15)
    
    def get_temp_f(self):
        return((self.get_temp_c()*1.8)+32)
    
    
        
        