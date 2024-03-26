import pyautogui
import time
import random
from pynput import keyboard

# Disable the fail-safe feature
pyautogui.FAILSAFE = False

def on_press(key):
    try:
        if key == keyboard.Key.shift_l and key.char == 'Q':
            return False  # Stop listener
    except AttributeError:
        pass

def auto_clicker(interval_range, button):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    try:
        while True:
            interval = random.randint(*interval_range) / 60
            pyautogui.click(button=button)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Program exited.")
        listener.stop()

# Set the interval range for clicks per minute (1-70) and specify the button as 'middle' for middle-clicks
interval_range = (1, 70)
button = 'middle'

auto_clicker(interval_range, button)