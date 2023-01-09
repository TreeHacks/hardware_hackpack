import utime
from machine import Pin, PWM

ir = Pin(21, Pin.IN)
servo = PWM(Pin(0)) #servo is connected to pin 0! 
servo.freq(50)

def cycle (position):
    servo.duty_u16(position)
    utime.sleep(0.01)

while True:
    try:
        print(ir.value())
        utime.sleep(1)
        if ir.value() == 0:
            print("Driving servo motor!")
            for pos in range(1000,9000,50):
                cycle(pos)
            for pos in range(9000,1000,-50):
                cycle(pos)
        else:
            print("No Interference Detected")
            utime.sleep(1)
            
    except KeyboardInterrupt:
        break
    
