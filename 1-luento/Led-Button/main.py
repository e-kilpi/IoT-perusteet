from machine import Pin

led = Pin(1, Pin.OUT)
nappi = Pin(4, Pin.IN, Pin.PULL_UP)

led.value(0)

while True:
  if nappi.value() == 0:
    led.value(1)
  else:
    led.value(0)