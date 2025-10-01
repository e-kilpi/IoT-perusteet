import machine
import time
import dht

sensor = dht.DHT22(machine.Pin(28))

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print(f"Temperature: {temperature:.1f} celsius")
        print(f"Humidity: {humidity:.1f}%")
    except OSError as e:
        print("Sensor read error:", e)

    time.sleep(2)