from gpiozero import Button
from time import sleep
from gpiozero import LED
btn = Button(2, pull_up=True)

prev = btn.is_pressed

while True:
    cur = btn.is_pressed

    if cur !=prev:
        if cur:
            print("pressed")
        else:
            print("released")

        prev=cur

    sleep(0.01)
while True:
   cur = btn.is_pressed
    if cur !=prev:
        led.on()
    else:
        led.off()

        prev=cur
    sleep(1)
