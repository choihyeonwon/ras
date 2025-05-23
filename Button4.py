from gpiozero import Button,LED
from time import sleep

led = LED(26)
button = Button(2)

while True:

    if button.is_pressed:
        led.on()
    else:
        led.off()
    sleep(0.1)

