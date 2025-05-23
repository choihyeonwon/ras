from gpiozero import Buzzer
import time

buzzor=Buzzer(3)

while True:
    buzzor.on()
    time.sleep(1)
    buzzor.off()
    time.sleep(1)

