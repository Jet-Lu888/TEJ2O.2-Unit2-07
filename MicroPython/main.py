"""
Created by: Jet Lu
Created on: Mar 2026
This module is a Micro:bit MicroPython program
"""

from microbit import *

Cookies = 0

while True:
    if button_a.is_pressed:
        cookies = (cookies +1)
        
        display.scroll(cookies)


