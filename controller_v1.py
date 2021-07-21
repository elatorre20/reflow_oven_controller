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
HEATER_UPPER = machine.PWM(machine.Pin(21), freq=3, duty_16=32768)
HEATER_LOWER = machine.PWM(machine.Pin(20), freq=3, duty_16=32768)
CONV_FAN     = machine.PWM(machine.Pin(19), freq=3, duty_16=32768)
LIGHT_IND    = machine.PWM(machine.Pin(18), freq=3, duty_16=32768)

#heating
pwm_period = 0.5

def heat(target, therm):
    error = therm.get_temp_c - target
    currentval = HEATER_UPPER.duty_u16()
    
    

# def get_scale():
#     #get temp units
#     while(True)
#         scale = ''
#         scale = input('select temperature scale from [C,F,K]:')
#         if scale in ['C', 'F', 'K']:
#             break
#         else:
#             print('Illegal input. Accepted values are: C, F, K')
            
def get_profile():
    #get temperature curve, in format:
    #[preheat temp, preheat time, soldering temp, soldering time, cooldown time]
    while(True):
        profile = [0,0,0,0,0]
        profile[0] = input('Enter preheat temp:')
        profile[1] = input('Enter preheat time:')
        profile[2] = input('Enter soldering temp:')
        profile[3] = input('Enter soldering time:')
        profile[4] = input('Enter cooldown time:')
        
        print('are these values correct? Y/N: ' + str(profile))
        ans = input('')
        if(ans.lower() in ['y', 'ye', 'yes']):
            break
    return([scale, profile])

#setup

spi1 = machine.SPI(1, baudrate=1000000,
                   polarity=0,
                   phase=0,
                   bits=8,
                   firstbit=SPI.MSB,
                   sck=SCK, mosi=MOSI, miso=MISO)

t0 = thermocouple_SPI(spi1, T0CS)

# scale = get_scale()
#assuming celsius for now to make life simple
profile = get_profile()

#enter control loop
t_start = utime.time()

while(utime.time() < (t_start + profile[1])):
    pass


    
print('all done!')