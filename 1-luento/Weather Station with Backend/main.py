import network
import time
import urequests
import dht
from machine import Pin

THINGSPEAK_API_KEY = "KEY GOES HERE"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

ssid = "Wokwi-GUEST"
password = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi.", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(28))

def send_to_thingspeak(temp):
    #Code that sends updates to ThingSpeak
    print("Data sent succesfully.")

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        print("Temperature:", temperature, "celsius")
        send_to_thingspeak(temperature)
    except Exception as e:
        print("Error reading sensor or sending data:", e)

    time.sleep(10)