import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

timer_start = 0

def button_handler(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print(f"Your reaction time was {reaction_time} milliseconds.")
    print("\nProgram complete.")

led.value(1)
utime.sleep(urandom.uniform(3, 6))

led.value(0)
timer_start = utime.ticks_ms()

button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)