from SPI_thermocouple import thermocouple_spi
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
