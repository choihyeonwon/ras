from gpiozero import LED, Button, Buzzer
from time import sleep, time
from random import uniform

led = LED(4)
button = Button(3, pull_up=True)
buzzer = Buzzer(13)

try:
    while True:
        sleep(uniform(1,5))

        led.on()
        print("두더지 등장!")
        start = time()
        caught= False

        while time() - start < 3:
            if button.is_pressed:
                caught = True
                break

        led.off()

        if caught:
            print("성공")
            buzzer.on()
            sleep(0.2)
            buzzer.off()
        else:
            print("실패")

except KeyboardInterrupt:
    print("\n게임을 종료 합니다.")
