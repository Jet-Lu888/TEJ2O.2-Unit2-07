"""
Created by: Jet Lu
Created on: Mar 2026
This module is a Micro:bit MicroPython program that runs Cookie Clicker.
"""

from microbit import *

cookies = 0

while True:
    # if button a is pressed, 1 cookie is added
    if button_a.was_pressed():  # used was pressed, so it won't add super fast
        cookies = cookies + 1
        display.clear()
        display.scroll(str(cookies))
    # resets the cookies
    if button_b.was_pressed():  # used was pressed, so it won't add super fast
        cookies = 0
        display.clear()
        display.scroll(str(cookies))
