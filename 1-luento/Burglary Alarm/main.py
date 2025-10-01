import machine
import utime

pir = machine.Pin(28, machine.Pin.IN)

buzzer = machine.Pin(5, machine.Pin.OUT)

while True:
    if pir.value() == 1:
        print("The alarm was tripped.")
        for i in range(5):
            buzzer.value(1)
            utime.sleep(0.2)
            buzzer.value(0)
            utime.sleep(0.2)

    utime.sleep(0.1)