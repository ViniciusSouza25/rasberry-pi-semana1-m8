
from machine import Pin
from time import sleep


LED1 = Pin(6, Pin.OUT)
LED2 = Pin(7, Pin.OUT)
LED3 = Pin(8, Pin.OUT)
LED4 = Pin(9, Pin.OUT)


while True:
    LED1.on()
    LED2.on()
    LED3.on()
    LED4.on()
    sleep(1)

    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()
    sleep(1)