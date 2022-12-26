import machine
import utime
from machine import Pin, PWM

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

servo = PWM(Pin(0)) #servo is connected to pin 0! 

servo.freq(50)

def cycle (position):
    servo.duty_u16(position)
    utime.sleep(0.01)

while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    #fan_status(temperature)
    if int(temperature) > 25:
        print("Driving servo motor!")
        for pos in range(1000,9000,50):
            cycle(pos)
        for pos in range(9000,1000,-50):
            cycle(pos)
    else:
        utime.sleep(2)
