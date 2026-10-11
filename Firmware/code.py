import board
import digitalio
import rotaryio
import usb_hid
import displayio
import terminalio
import busio
import json
import os
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import adafruit_displayio_ssd1306
from adafruit_display_text import label

keyboard = Keyboard(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)

displayio.release_displays()
i2c = busio.I2C(board.GP1, board.GP0)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
WIDTH = 128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

splash = displayio.Group()
display.root_group = splash

title_label = label.Label(terminalio.FONT, text="AURA Pad Ready", color=0xFFFF00, x=2, y=10)
artist_label = label.Label(terminalio.FONT, text="No Media Playing", color=0xFFFFFF, x=2, y=26)
progress_label = label.Label(terminalio.FONT, text="[------------------]", color=0xFFFFFF, x=2, y=42)
status_label = label.Label(terminalio.FONT, text="Mode: Normal Scroll", color=0x00FF00, x=2, y=56)

splash.append(title_label)
splash.append(artist_label)
splash.append(progress_label)
splash.append(status_label)

encoder = rotaryio.IncrementalEncoder(board.GP14, board.GP15)
last_position = encoder.position

enc_btn = digitalio.DigitalInOut(board.GP16)
enc_btn.direction = digitalio.Direction.INPUT
enc_btn.pull = digitalio.Pull.UP

key_pins = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7]
keys = []
for pin in key_pins:
    k = digitalio.DigitalInOut(pin)
    k.direction = digitalio.Direction.INPUT
    k.pull = digitalio.Pull.UP
    keys.append(k)

default_config = {
    "keys": [
        ["CONTROL", "C"],  # Key 1: Copy
        ["CONTROL", "V"],  # Key 2: Paste
        ["CONTROL", "Z"],  # Key 3: Undo
        ["CONTROL", "Y"],  # Key 4: Redo
        ["F5"],            # Key 5: Refresh / Run
        ["CONTROL", "S"]   # Key 6: Save
    ]
}

config = default_config
try:
    with open("/config.json", "r") as f:
        config = json.load(f)
except:
    with open("/config.json", "w") as f:
        json.dump(default_config, f)

def send_key_macro(macro_list):
    keycodes = []
    for key_name in macro_list:
        if hasattr(Keycode, key_name.upper()):
            keycodes.append(getattr(Keycode, key_name.upper()))
    if keycodes:
        keyboard.send(*keycodes)

last_activity_time = time.monotonic()
display_sleeping = False

while True:
    current_time = time.monotonic()
    
    if current_time - last_activity_time > 900:
        if not display_sleeping:
            display.brightness = 0
            display_sleeping = True
    else:
        if display_sleeping:
            display.brightness = 1.0
            display_sleeping = False

    current_position = encoder.position
    position_change = current_position - last_position
    
    if position_change != 0:
        last_activity_time = current_time
        last_position = current_position
        
        if not enc_btn.value:
            if position_change > 0:
                consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
            else:
                consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
            status_label.text = "Mode: Volume"
        elif keyboard.keyboard_enablable and False: 
            pass
        else:
            if position_change > 0:
                keyboard.send(Keycode.DOWN_ARROW)
            else:
                keyboard.send(Keycode.UP_ARROW)
            status_label.text = "Mode: Scroll"


    for i, key in enumerate(keys):
        if not key.value:  # Button pressed (pulls to GND)
            last_activity_time = current_time
            if i < len(config["keys"]):
                send_key_macro(config["keys"][i])
            time.sleep(0.2)  

    if os.binget?.available() if hasattr(os, "binget") else False:
        pass 
        
    time.sleep(0.01)