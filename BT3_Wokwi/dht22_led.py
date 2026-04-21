from machine import Pin
import dht
import time

# LED
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

# DHT22
sensor = dht.DHT22(Pin(16))

while True:
    try:
        sensor.measure()

        temp = sensor.temperature()
        hum = sensor.humidity()

        t = time.localtime()
        ts = f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"

        print(f"[{ts}] Temp: {temp:.1f}C | Humidity: {hum:.1f}%")

        # CANH BAO
        if temp > 30:
            red.value(1)
            yellow.value(0)
            green.value(0)
            print("  >> CANH BAO: NHIET DO CAO!")

        elif hum > 80:
            red.value(0)
            yellow.value(1)
            green.value(0)
            print("  >> CANH BAO: DO AM CAO!")

        else:
            red.value(0)
            yellow.value(0)
            green.value(1)
            print("  Binh thuong.")

    except Exception as e:
        print("Loi:", e)

    time.sleep(2)
