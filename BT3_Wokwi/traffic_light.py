from machine import Pin
from time import sleep

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:

    # Neu bam nut -> cho nguoi di bo qua
    if button.value() == 0:
        red.value(1)
        yellow.value(0)
        green.value(0)
        sleep(5)
        continue

    # Binh thuong
    red.value(1)
    yellow.value(0)
    green.value(0)
    sleep(3)

    green.value(1)
    red.value(0)
    yellow.value(0)
    sleep(3)

    yellow.value(1)
    red.value(0)
    green.value(0)
    sleep(1)
