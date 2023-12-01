from pynput import mouse
from time import sleep
from pyautogui import hotkey

DELAY = 0.01

print("Waiting for GPU fully loaded...")
sleep(10)  # to ensure that GPU fully loaded in startup
print("Prosees is running...")


def move_to_next_desktop():
    hotkey('ctrl', 'win', 'right')  # the shortcut for the next desktop
    sleep(DELAY)


def move_to_previous_desktop():
    hotkey('ctrl', 'win', 'left')
    sleep(DELAY)


def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.x2:  # the forward button
            move_to_next_desktop()
        elif button == mouse.Button.x1:  # the backward button
            move_to_previous_desktop()


with mouse.Listener(on_click=on_click) as listener:
    listener.join()
