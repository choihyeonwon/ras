from gpiozero import Button

btn = Button(2, pull_up=True)

while True:
    btn.wait_for_press()
    print("pressed")

    btn.wait_for_release()
    print("released")
