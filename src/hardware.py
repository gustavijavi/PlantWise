import board
import digitalio
import analogio
import time
import adafruit_dht
import adafruit_character_lcd.character_lcd as character_lcd

photocell = analogio.AnalogIn(board.A0)
dht_device = adafruit_dht.DHT11(board.D5)

btn_up = digitalio.DigitalInOut(board.A1)
btn_up.direction = digitalio.Direction.INPUT
btn_up.pull = digitalio.Pull.UP

btn_down = digitalio.DigitalInOut(board.A2)
btn_down.direction = digitalio.Direction.INPUT
btn_down.pull = digitalio.Pull.UP

btn_select = digitalio.DigitalInOut(board.A3)
btn_select.direction = digitalio.Direction.INPUT
btn_select.pull = digitalio.Pull.UP

led_red = digitalio.DigitalInOut(board.A4)
led_red.direction = digitalio.Direction.OUTPUT
led_green = digitalio.DigitalInOut(board.A5)
led_green.direction = digitalio.Direction.OUTPUT
led_blue = digitalio.DigitalInOut(board.SCK)
led_blue.direction = digitalio.Direction.OUTPUT


def get(): #returns temp, humidity, light
    temperature_c = dht_device.temperature
    humidity = dht_device.humidity
    light = photocell.value
    # Convert to Fahrenheit
    temperature_f = temperature_c * (9 / 5) + 32
    return temperature_f,humidity,light


#hardware:https://docs.circuitpython.org/projects/charlcd/en/latest/
#LCD

# LCD Setup
lcd_rs = digitalio.DigitalInOut(board.D13)
lcd_en = digitalio.DigitalInOut(board.D12)
lcd_d4 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d6 = digitalio.DigitalInOut(board.D9)
lcd_d7 = digitalio.DigitalInOut(board.D6)
lcd_columns = 16
lcd_rows = 2
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# lcd.message=flower.getName()
def display(line1, line2):
    lcd.clear()
    lcd.message = line1 + "\n" + line2

def set_led(r, g, b):
    led_red.value = r
    led_green.value = g
    led_blue.value = b

# while True:
#     try:
#         temp, humid, light=get()

#     except RuntimeError as e:
#         # Reading a sensor is guaranteed to fail once in a while, retry
#         print(f"Reading error: {e.args[0]}")
#         time.sleep(2)  # Wait at least 2 seconds between readings
#         continue

#     time.sleep(2)  # Wait at least 2 seconds between readings