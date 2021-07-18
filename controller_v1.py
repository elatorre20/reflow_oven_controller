import SPI_thermocouple
import machine
import utime
from micropython import const

#definitions
#thermocouple SPI: GPIO 10-13

#thermocouple chip select
SCK  = machine.Pin(10)
MOSI = machine.Pin(11)
MISO = machine.Pin(12)
T0CS = machine.Pin(13, Pin.OUT)

#relay pins
HEATER_UPPER = machine.Pin(21, Pin.OUT)
HEATER_LOWER = machine.Pin(20, Pin.OUT)
CONV_FAN     = machine.Pin(19, Pin.OUT)
LIGHT_IND    = machine.Pin(18, Pin.OUT)

#setup

spi1 = machine.SPI(1, baudrate=1000000,
                   polarity=0,
                   phase=0,
                   bits=8,
                   firstbit=SPI.MSB,
                   sck=SCK, mosi=MOSI, miso=MISO)

t0 = thermocouple_SPI(spi1, T0CS)


