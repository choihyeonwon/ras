from gpiozero import LED
import time
led=LED(12)
i=0
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    i+=1
    if i==10:
        break



