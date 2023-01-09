import utime
from machine import Pin, PWM

servo = PWM(Pin(0)) #servo is connected to pin 0! 
servo.freq(50)

def cycle (position):
    servo.duty_u16(position)
    utime.sleep(0.01)

while True:
    print("Driving servo motor!")
    for pos in range(1000,9000,50):
        cycle(pos)
    for pos in range(9000,1000,-50):
        cycle(pos)
    utime.sleep(2)
            
    
