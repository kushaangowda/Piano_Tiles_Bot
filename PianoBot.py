from pyautogui import *
import pyautogui
import keyboard

# Tile1 X:550 Y:434
# Tile2 X:626 Y:434
# Tile3 X:714 Y:434
# Tile4 X:797 Y:434

while keyboard.is_pressed('q') == False:
	if pyautogui.pixel(550,434)[0] == 0:
		pyautogui.mouseDown(x=550,y=434)
	if pyautogui.pixel(626,434)[0] == 0:
		pyautogui.mouseDown(x=626,y=434)
	if pyautogui.pixel(714,434)[0] == 0:
		pyautogui.mouseDown(x=714,y=434)
	if pyautogui.pixel(797,434)[0] == 0:
		pyautogui.mouseDown(x=797,y=434)